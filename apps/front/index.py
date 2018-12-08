from apps.front import bp
from apps.models import db
from flask import render_template, request, redirect, url_for, current_app
from apps.forms.custom import CustomForm
from apps.models.custom import Custom
from apps.api import Api
@bp.route('/')
def index():
    return render_template("front/index1.html")


@bp.route('/submit_info',methods=['POST','GET'])
def submit_info():
    if request.method == "GET":
        return render_template("front/index.html")
    else:

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
            result = Custom.query.filter_by(phone_num=customer.phone_num).first()
            if result:
                return Api.params_error(msg="此手机号已提交")
            else:
                db.session.add(customer)
                db.session.commit()
                return Api.success()
        else :
            return Api.params_error(msg=form.get_error)

@bp.route('/gift')
def gift():
    phone_num = request.args.get('phone_num')
    custom = Custom.query.filter_by(phone_num=phone_num).first()
    gift = custom.get_gift(current_app.config['GIFTS'])
    custom.gift = gift
    db.session.commit()
    return render_template('front/gift.html',phone_num=phone_num,gift=gift),{'Content-type':'text/html'}
