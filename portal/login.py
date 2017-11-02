import re
from db.models import Customer, session
from views import *
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_Hans'
from flask_babel import gettext as _
from datetime import datetime, timedelta
from security import decrypt_password, encrypt_password


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '').strip()
    email = request.form.get('email', '').strip()
    decipher_password = decrypt_password(password)
    result = validate(username, decipher_password, email)
    if result is True:
        encipher_password = encrypt_password(username, decipher_password)
        status = _save(username, encipher_password, email)
        if status:
            return render_200(_('register successfully'))
        return render_200(_('register failed'))
    return result


def validate(username, password, email):
    if username and password and email:
        if not re.match(r'^[a-zA-Z][a-zA-Z0-9]{3,19}$', username):
            return render_400(_('The username must be startswith latter 4-20 bit'))
        elif not re.match(r'^{8,20}$', password):
            return render_400(_('The password must be 8-20 character'))
        elif not re.match(r'^[a-zA-Z0-9]+([._\\-\\+]*[a-zA-Z0-9])*@([a-zA-Z0-9]+'
                          r'[-a-zA-Z0-9]*[a-zA-Z0-9]+.){1,63}[a-zA-Z0-9]+$', email):
            return render_400(_('The email format invalid'))
        return True
    return render_404(_('The username or password or email does not None'))


def _save(username, password, email):
    try:
        print username, password, email
        customer = Customer(username=username, password=password, email=email)
        session.add(customer)
        session.commit()
        session.close()
        return True
    except Exception, e:
        return False


@app.route('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    customer = Customer(username=username, password=password)
    if len(customer) == 1:
        # redirect_to_index = redirect('/index')
        # response = current_app.make_response(redirect_to_index )
        # response.set_cookie('cookie_name',value='values')
        # return response
        resp = make_response(render_template('*.html'))
        expires=datetime.today() + timedelta(days=30)
        resp.set_cookie('identification', username, expires=expires)
        return resp
    return render_template('index.html', {'data': _('username or password invalid')})

