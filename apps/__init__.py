import os
import random
from apps.setting import config
import click
from flask import Flask
from apps.front import bp as front_bp
from apps.cms import bp as cms_bp
from apps.cms import login_manager
from apps.models import db, User, Custom
from flask_wtf.csrf import CSRFProtect
from faker import Faker

def create_app():
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIG','development')
    app.config.from_object(config[config_name])
    db.init_app(app)
    db.create_all(app=app)
    login_manager.init_app(app)
    csrf = CSRFProtect()
    csrf.init_app(app)
    register_bp(app)
    command(app)
    return app


def register_bp(app):
    app.register_blueprint(front_bp)
    app.register_blueprint(cms_bp)



def command(app):
    @app.cli.command()
    def create_admin():
        db.create_all()
        username = "admin"
        password = "123456"
        name = "admin"
        user = User(username=username,password=password,name=name,permission="管理员")
        db.session.add(user)
        db.session.commit()
        click.echo("success")

    @app.cli.command()
    def create_data():
        faker = Faker('zh_CN')
        for i in range(100):
            info = Custom(
                name = faker.name(),
                phone_num = faker.phone_number(),
                addr = faker.address(),
                year = random.randint(1,100),
                work = '职员',
                money = random.randint(1,10),
                bank = '建行',
                custom = '是',
            )
            db.session.add(info)
        db.session.commit()
        click.echo('添加数据成功')

