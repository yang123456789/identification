import re
from db.models import Customer, session
from views import *
from flask_babel import gettext as _
from datetime import datetime, timedelta
from security import decrypt_password, encrypt_password, generate_customer_id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    decipher_password = decrypt_password(password)
    result = validate_register(username, decipher_password, email)
    if result is True:
        username, email = username.strip(), email.strip()
        encipher_password = encrypt_password(username, decipher_password)
        status = _save(username, encipher_password, email)
        if status:
            return render_200(_('register successfully'))
        return render_400(_('register failed'))
    return result


def validate_register(username, password, email):
    if username and password and email:
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9]{3,19}$', username):
            return render_400(_('The username must be startswith latter 4-20 bit'))
        elif len(password) < 8 or len(password) > 20:
            return render_400(_('The password must be 8-20 character'))
        elif not re.match(r'^[a-zA-Z0-9]+([._\\-\\+]*[a-zA-Z0-9])*@([a-zA-Z0-9]+'
                          r'[-a-zA-Z0-9]*[a-zA-Z0-9]+.){1,63}[a-zA-Z0-9]+$', email):
            return render_400(_('The email format invalid'))
        return True
    return render_404(_('The username or password or email does not None'))


def _save(username, password, email):
    try:
        customer_id = generate_customer_id()
        customer = Customer(customer_id=customer_id, username=username, password=password, email=email)
        session.add(customer)
        session.commit()
        session.close()
        return True
    except Exception, e:
        logger.error(e)
        return False


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    validate = validate_login(username, password)
    if validate is True:
        username, password = username.strip(), password.strip()
        customer = Customer(username=username, password=password)
        if len(customer) == 1:
            resp = make_response(render_template('*.html'))
            if request.cookies.get('identify') is None:
                expires = datetime.today() + timedelta(days=30)
                resp.set_cookie('identify', username, expires=expires)
                return resp
            return render_200('')
        return render_404(_('Not yet registered. Please register'))
    return validate


def validate_login(username, password):
    if not username:
        return render_404(_('The username does not None'))
    elif not password:
        return render_404(_('The password does not None'))
    return True
