from flask import Blueprint

# 注册蓝图 指定静态目录
# web = Blueprint('web', __name__, template_folder='templates')
web = Blueprint('web', __name__)

from app.web import book
from app.web import user