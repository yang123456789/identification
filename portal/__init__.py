from flask import Flask
from flask_babel import Babel
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans'
babel = Babel(app)
logger = app.logger

import portal.login
