from apps.front import bp
from apps.models import db
from flask import render_template,request,jsonify
from apps.forms.custom import CustomForm
from apps.models.custom import Custom
from apps.api import Api
@bp.route('/')
def index():
    return render_template("front/index.html")


@bp.route('/submit_info',methods=['POST'])
def submit_info():
    form = CustomForm(request.form)
    if form.validate():
        name = form.name.data
        phone_num = form.phone_num.data
        addr = form.addr.data
        money = form.money.data
        year = form.year.data
        work = form.work.data
        bank = form.bank.data
        custom = form.custom.data
        customer = Custom(name=name,phone_num=phone_num,addr=addr,year=year,
                          money=money,work=work,bank=bank,custom=custom)
        result = Custom.query.filter_by(phone_num=customer.phone_num).all()
        if len(result) >= 3:
            return Api.params_error(msg="此手机号提交已超过3次")
        else:
            db.session.add(customer)
            db.session.commit()
            return Api.success(msg="提交成功,感谢您的参与")
    else :
        return Api.params_error(msg=form.get_error)
