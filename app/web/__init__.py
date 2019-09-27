from flask import Blueprint


# flask中的蓝图 blueprint机制
web = Blueprint('web', __name__)

from app.web import book
from app.web import user

