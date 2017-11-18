import re
from db.models import Customer, db
from views import *
from flask_babel import gettext as _
from security import decrypt_password, encrypt_password, generate_customer_id, generate_cookie, check_password
from portal import cache


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
        db.session.add(customer)
        db.session.commit()
        db.session.close()
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
        username, password = username.strip(), decrypt_password(password)
        customer = Customer.query.filter_by(username=username).all()
        if len(customer) == 1:
            pwhash = username+password
            pwd = customer[0].password
            if check_password(pwd, pwhash):
                cookie = generate_cookie(username, password)
                if add_cookie(cookie, {username: password}):
                    return render_200(cookie)
                return render_400(_('login failed'))
            return render_400(_('The password invalid'))
        return render_400(_('The username invalid'))
    return validate


def validate_login(username, password):
    if not username:
        return render_404(_('The username does not None'))
    elif not password:
        return render_404(_('The password does not None'))
    return True


def add_cookie(key, value, timeout=4*60*60):
    try:
        cache.set(key, value, timeout=timeout)
        return True
    except Exception, e:
        logger.error(e)
        return False
