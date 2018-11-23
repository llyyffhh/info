from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import Length,equal_to
class UserForm(BaseForm):
    username = StringField(validators=[Length(min=4,max=10,message='用户名必须为4-10位')])
    password =StringField(validators=[Length(min=6,max=16,message='密码必须为6-16位')])

class ResetPwdForm(BaseForm):
    old_password = StringField(validators=[Length(min=6,max=16,message="密码必须为6-16位")])
    new_password = StringField(validators=[Length(min=6,max=16,message="密码必须为6-16位")])
    new_password1 = StringField(validators=[equal_to('new_password',message="两次输入密码不一致")])

class AddUserForm(UserForm):
    name = StringField(validators=[Length(max=4,message="姓名长度有误")])
    password1 = StringField(validators=[equal_to("password",message='两次输入密码不一致')])