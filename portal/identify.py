from views import *
import re
from flask_babel import gettext as _
from config import identify, CARD
import requests
import requests.exceptions


@app.route('/query')
@login_required
def inquire():
    return render_template('query.html')


@app.route('/query/info', methods=['POST'])
@login_required
def query_card():
    card = request.form.get('card')
    if card:
        card = card.strip()
        validate = validate_card(card)
        if validate is True:
            result = Identify(card).info_query()
            return result
        return validate
    return render_404(_('The card does not None'))


@app.route('/query/leak', methods=['POST'])
@login_required
def leak_card():
    card = request.form.get('card')
    if card:
        card = card.strip()
        validate = validate_card(card)
        if validate is True:
            result = Identify(card).leak_query()
            return result
        return validate
    return render_404(_('The card does not None'))


@app.route('/query/loss', methods=['POST'])
@login_required
def loss_card():
    card = request.form.get('card')
    if card:
        card = card.strip()
        validate = validate_card(card)
        if validate is True:
            result = Identify(card).loss_query()
            return result
        return validate
    return render_404(_('The card does not None'))


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


class Identify(object):
    AppKey = CARD['key']

    def __init__(self, card):
        self.card = card

    def request(self, url, dtype='json'):
        data = dict(
            key=self.AppKey,
            dtype=dtype,
            cardno=self.card
        )
        try:
            req = requests.get(url, params=data, timeout=10)
            if req.status_code is 200:
                content = req.json()
                logger.info(content)
                if content.get('resultcode') == '200':
                    return render_200(content.get('result'))
                return render_json(int(content.get('resultcode')), content.get('reason'))
        except requests.exceptions.ConnectTimeout, e:
            logger.error(e)
            return render_200({})
        except requests.exceptions.ConnectionError, e:
            logger.error(e)
            return render_200({})
        except requests.exceptions.RequestException, e:
            logger.error(e)
            return render_200({})

    def info_query(self):
        url = CARD['info_url']
        result = self.request(url)
        return result

    def leak_query(self):
        url = CARD['leak_url']
        result = self.request(url)
        return result

    def loss_query(self):
        url = CARD['loss_url']
        result = self.request(url)
        return result

