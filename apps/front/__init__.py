from flask import Blueprint

bp = Blueprint("front",__name__)

from ..front import index

