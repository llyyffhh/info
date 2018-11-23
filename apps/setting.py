import os

class BaseConfig:
    JSON_AS_ASCII = False

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+cymysql://root:@127.0.0.1:3306/info"
    SECRET_KEY = "strong sting"

class ProductionConfig(BaseConfig):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = os.urandom(64)

config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig
}




