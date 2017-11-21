from views import *
import re
from flask_babel import gettext as _
from config import identify


@app.route('/query')
def inquire():
    return render_template('query.html')


@app.route('/query/info', methods=['POST'])
def query_card():
    card = request.form.get('card')
    validate = validate_card(card.strip())
    if validate is True:
        pass
    return validate


def validate_card(card):
    if len(card) == 15:
        area = card[:2]
        if area not in identify['area']:
            return render_404(_('The card area illegal'))
        return _validate_fifteen_card(card)
    elif len(card) == 18:
        area = card[:2]
        if area not in identify['area']:
            return render_404(_('The card area illegal'))
        return _validate_eighteen_card(card)
    return render_400(_('The card figure invalid'))


def _validate_fifteen_card(card):
    if (int(card[6:8])+1900) % 4 == 0 or \
                ((int(card[6:8])+1900) % 100 == 0 and
                    (int(card[6:8])+1900) % 4 == 0):
        # birthday
        erg = re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)'
                         '(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)'
                         '(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$')
    else:
        erg = re.compile('[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)'
                         '(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)'
                         '(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$')
    if re.match(erg, card):
        return True
    return render_400(_('The card invalid'))


def _validate_eighteen_card(card):
    card_list = list(card)
    if int(card[6:10]) % 4 == 0 or \
            (int(card[6:10]) % 100 == 0 and int(card[6:10]) % 4 == 0):
        # runnian
        erg = re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)'
                         '(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)'
                         '(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$')
    else:
        # pingnian
        erg = re.compile('[1-9][0-9]{5}19[0-9]{2}((01|03|05|07|08|10|12)'
                         '(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)'
                         '|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$')
    if re.match(erg, card):
        s = (int(card_list[0]) + int(card_list[10])) * 7 + \
            (int(card_list[1]) + int(card_list[11])) * 9 + \
            (int(card_list[2]) + int(card_list[12])) * 10 + \
            (int(card_list[3]) + int(card_list[13])) * 5 + \
            (int(card_list[4]) + int(card_list[14])) * 8 + \
            (int(card_list[5]) + int(card_list[15])) * 4 + \
            (int(card_list[6]) + int(card_list[16])) * 2 + \
            int(card_list[7]) * 1 + int(card_list[8]) * 6 + \
            int(card_list[9]) * 3
        y = s % 11
        m = 'F'
        jym = '10X98765432'
        m = jym[y]
        if m == card_list[17]:
            return True
        return render_400(_('The card invalid'))
    return render_400(_('The card invalid'))
