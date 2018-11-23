from flask import jsonify

from apps.models import db
from datetime import date
class Custom(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10), nullable=False)
    phone_num = db.Column(db.String(20),nullable=False)
    addr = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(10),nullable=False)
    money = db.Column(db.String(5), nullable=False)
    work = db.Column(db.String(10), nullable=False)
    bank = db.Column(db.String(10),nullable=False)
    custom = db.Column(db.String(2),nullable=False)
    join_time= db.Column(db.DateTime,default=date.today)

    @staticmethod
    def get_detail(limit,page):
        users = []
        result = Custom.query.limit(limit).offset((page-1)*limit)
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
            detail['join_time'] = Custom.get_time(data.join_time)
            users.append(detail)
        return users

    @staticmethod
    def custom_api(limit,page):
        api = {
            'code': 0,
            'count':len(Custom.query.all()),
            'data': Custom.get_detail(limit,page)
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

