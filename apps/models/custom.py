from flask import jsonify
from random import choice
from apps.models import db
from datetime import date
class Custom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    phone_num = db.Column(db.String(20),nullable=False,unique=True)
    addr = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10),nullable=False)
    money = db.Column(db.String(5), nullable=False)
    work = db.Column(db.String(10), nullable=False)
    bank = db.Column(db.String(10),nullable=False)
    custom = db.Column(db.String(2),nullable=False)
    gift = db.Column(db.String(20),nullable=True)
    join_time= db.Column(db.DateTime,default=date.today)

    @staticmethod
    def get_detail(limit,page,key=None):
        users = []
        if not key:
            result = Custom.query.limit(limit).offset((page-1)*limit)
        elif Custom.is_num(key):
            result = Custom.query.filter_by(phone_num=key).limit(limit).offset((page-1)*limit)
        else :
            result = Custom.query.filter_by(name=key).limit(limit).offset((page-1)*limit)
        for data in result:
            detail = {}
            detail["id"] = str(data.id)
            detail['name'] = data.name
            detail['phone_num'] = data.phone_num
            detail['addr'] = data.addr
            detail['year'] = data.year
            detail['money'] = data.money
            detail['work'] = data.work
            detail['bank'] = data.bank
            detail['custom'] = data.custom
            detail['gift'] = data.gift
            detail['join_time'] = Custom.get_time(data.join_time)
            users.append(detail)
        return users

    @staticmethod
    def custom_api(limit,page,key=None):
        if not key:
            count = len(Custom.query.all())
        elif Custom.is_num(key):
            count = len(Custom.query.filter_by(phone_num=key).all())
        else :
            count = len(Custom.query.filter_by(name=key).all())
        api = {
            'code': 0,
            'count':count,
            'data': Custom.get_detail(limit,page,key)
        }
        return jsonify(api)

    @classmethod
    def get_total(cls):
        result = cls.query.all()
        return len(result)

    @classmethod
    def today_data(cls):
        today = date.today()
        result = cls.query.filter_by(join_time=today).all()
        return len(result)

    @staticmethod
    def get_time(time):
        join_time = time.strftime("%Y-%m-%d")
        return join_time

    def get_gift(self,gifts):
        gift = choice(gifts)
        return gift

    @staticmethod
    def is_num(key):
        return key.isdigit()

