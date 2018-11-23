
from flask import Blueprint,render_template
from flask_login import LoginManager
from apps.models.user import User

bp = Blueprint("cms",__name__,url_prefix='/cms')
login_manager = LoginManager()
login_manager.login_view = 'cms.login'

from apps.cms import index,user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('cms/404.html'),404
