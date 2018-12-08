from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import Length,regexp,DataRequired,InputRequired


class CustomForm(BaseForm):
    name = StringField(validators=[Length(min=2,max=4,message='姓名长度有误')])
    phone_num = StringField(validators=[regexp(r"1[3456789]\d{9}",message='手机号格式有误')])
    addr = StringField(validators=[DataRequired(message="地址不能为空"),Length(max=50,message='地址太长了')])
    money = StringField(validators=[DataRequired(message="收入未输入")])
    year = StringField(validators=[DataRequired(message="年龄未输入")])
    work = StringField(validators=[DataRequired(message="职业未选择")])
    bank = StringField(validators=[DataRequired(message="银行未选择")])
    custom = StringField(validators=[DataRequired()])



