from flask import Flask
from flask_babel import Babel
from flask_cache import Cache
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans'
babel = Babel(app)
logger = app.logger
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_HOST': '123.58.244.170',
                           'CACHE_REDIS_PORT': 6379, 'CACHE_REDIS_DB': 1, 'CACHE_REDIS_PASSWORD': 'SYHXsqq@1233',
                           'CACHE_DEFAULT_TIMEOUT': 20})

from portal import login, identify
