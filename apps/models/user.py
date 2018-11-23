from functools import wraps

from apps.models import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from flask import jsonify, redirect, url_for


class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),nullable=False,unique=True)
    __password = db.Column(db.String(128),nullable=False)
    name = db.Column(db.String(5),nullable=False)
    join_time = db.Column(db.DateTime,default=datetime.now)
    permission = db.Column(db.String(5),default="操作员")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,raw_pwd):
        self.__password = generate_password_hash(raw_pwd)

    def check_pwd(self,pwd):
        return check_password_hash(self.__password,pwd)

    @staticmethod
    def user_detail():
        result = []
        users = User.query.all()
        for x in users:
            detail = {}
            detail["username"] = x.username
            detail["name"] = x.name
            detail["join_time"] = User.get_time(x.join_time)
            detail["permission"] = x.permission
            result.append(detail)
        return result

    @staticmethod
    def user_api():
        api = {
            'code':0,
            'count':len(User.query.all()),
            'data': User.user_detail()
            }
        return jsonify(api)

    @staticmethod
    def get_time(time):
        join_time = time.strftime("%Y-%m-%d")
        return join_time


    def has_permission(self,permission):
        return True if permission == '管理员' else False
    @classmethod
    def get_total(cls):
        result = cls.query.all()
        return len(result)

def permission_required(func):
    @wraps(func)
    def inner(*args,**kwargs):
        user = current_user
        if user.has_permission(user.permission):
            return func(*args,**kwargs)
        else:
            return redirect(url_for('cms.index'))
    return inner