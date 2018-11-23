from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from apps.models.custom import Custom
from apps.models.user import User