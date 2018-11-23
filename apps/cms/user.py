from flask_login import login_user,login_required,current_user
from apps.api import Api
from apps.cms import bp
from apps.models.user import User,permission_required
from apps.models import db
from apps.forms.user import UserForm, ResetPwdForm, AddUserForm
from flask import request,render_template,redirect,url_for,views

class LoginView(views.MethodView):
    def get(self,message=None):
        return render_template("cms/login.html",message=message)

    def post(self):
        form = UserForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_pwd(password):
                login_user(user)
                return redirect(url_for("cms.index"))
            else:
                message = "用户名或密码错误"
                return self.get(message=message)
        else:
            message = form.get_error
            return self.get(message=message)

@bp.route('/logout')
@login_required
def logout():
    login_user(current_user)
    return redirect(url_for("cms.login"))

@bp.route('/reset_pwd',methods=["GET","POST"])
@login_required
def reset_pwd():
    if request.method == "GET":
        return render_template("cms/reset_pwd.html")
    else :
        form = ResetPwdForm(request.form)
        if form.validate():
            raw_pwd = form.old_password.data
            new_pwd = form.new_password.data
            user = User.query.filter_by(username=current_user.username).first()
            if user.check_pwd(raw_pwd):
                user.password = new_pwd
                db.session.commit()
                return Api.success("密码修改成功")
            else:
                return Api.params_error(msg="原密码错误")
        else:
            return Api.params_error(msg=form.get_error)

@bp.route("/users")
@login_required
@permission_required
def users():
    return render_template("cms/users1.html",users=User.user_detail())

@bp.route("/user_detail")
@login_required
@permission_required
def user_detail():
    return User.user_api()


@bp.route("/add_user",methods=["GET","POST"])
@login_required
@permission_required
def add_user():
    if request.method == "GET":
        return render_template("cms/add_user.html")
    else :
        form = AddUserForm(request.form)
        if form.validate():
            username = form.username.data
            name = form.name.data
            password = form.password.data
            user = User(username=username,name=name,password=password)
            result = User.query.filter_by(username=username).first()
            if result:
                return Api.params_error("该用户已存在，不能重复添加")
            else:
                db.session.add(user)
                db.session.commit()
                return Api.success("添加用户成功")
        else:
            return Api.params_error(form.get_error)

@bp.route("/del_user",methods=["GET","POST"])
@login_required
@permission_required
def del_user():
    if request.method == "GET":
        return render_template("cms/del_user.html",users=User.user_detail())
    else:
        username = request.form.get("interest")
        user = User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return Api.success("删除成功")
        else:
            return Api.params_error("无此用户")



bp.add_url_rule('/login',view_func=LoginView.as_view('login'))