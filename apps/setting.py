import secrets
import os
class BaseConfig:
    JSON_AS_ASCII = False
    GIFTS = ['礼品1','礼品2','礼品3','礼品4','礼品5']

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:@127.0.0.1:3306/info"
    SECRET_KEY = "strong sting"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = secrets.token_urlsafe(16)

config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}




