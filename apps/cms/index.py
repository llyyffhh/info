from apps.api import Api
from apps.cms import bp
from flask_login import login_required
from flask import render_template, request,jsonify
from apps.models.custom import Custom
from apps.models import db, User


@bp.route('/index')
@login_required
def index():
    data = {
        'today_data' : str(Custom.today_data()),
        'total_data' : str(Custom.get_total()),
        'total_user' : str(User.get_total())
    }
    return render_template('cms/index1.html',**data)


@bp.route('/custom')
@login_required
def custom():
    return render_template('cms/custom.html')

@bp.route('/custom_detail')
@login_required
def custom_detail():
    limit = int(request.args.get('limit'))
    page = int(request.args.get('page'))
    return Custom.custom_api(limit,page)

@bp.route('/delete_custom',methods=["POST"])
@login_required
def delete_custom():
    id = request.form.get('id')
    if id:
        customer = Custom.query.get(id)
        db.session.delete(customer)
        db.session.commit()
        return Api.success(msg='删除成功')
    else:
        return Api.params_error(msg='无法删除')

@bp.route('/search_data',methods=["POST"])
@login_required
def search_data():
    limit = int(request.form.get('limit'))
    page = int(request.form.get('page'))
    key = request.form.get('data')
    return Custom.custom_api(limit=limit,page=page,key=key)

