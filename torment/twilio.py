import requests

from torment import settings

BASE_URL = 'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/{endpoint}'

# Get these credentials from http://twilio.com/user/account
ACCOUNT_SID = settings.TWILIO_ACCOUNT_SID
AUTH_TOKEN = settings.TWILIO_AUTH_TOKEN
FROM_NUMBER = settings.TWILIO_FROM_NUMBER


def make_call(to, call_url):
    url = BASE_URL.format(account_sid=ACCOUNT_SID, endpoint='Calls.json')
    data = {'From': FROM_NUMBER,
            'To': to,
            'Url': call_url,
            'Method': 'GET',
            'IfMachine': 'Hangup'
            }
    r = requests.post(url, data=data, auth=(ACCOUNT_SID, AUTH_TOKEN))
    r.raise_for_status()


def send_text(to, text=None, image_url=None):
    url = BASE_URL.format(account_sid=ACCOUNT_SID, endpoint='Messages.json')
    data = {'From': FROM_NUMBER, 'To': to}
    if text:
        data['Body'] = text
    if image_url:
        data['MediaUrl'] = image_url
    r = requests.post(url, data=data, auth=(ACCOUNT_SID, AUTH_TOKEN))
    r.raise_for_status()
