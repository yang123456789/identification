import logging
from flask import Flask
app = Flask(__name__)

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('flask.log', encoding='UTF-8')
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(host='localhost', port=9530)
