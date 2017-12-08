from flask import Flask
from flask_babel import Babel
from flask_cache import Cache
from config import REDIS
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans'
babel = Babel(app)
logger = app.logger
cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_HOST': REDIS['host'],
                           'CACHE_REDIS_PORT': REDIS['port'], 'CACHE_REDIS_DB': REDIS['db'],
                           'CACHE_REDIS_PASSWORD': REDIS['password'],
                           'CACHE_DEFAULT_TIMEOUT': REDIS['timeout']})

from portal import login, identify
