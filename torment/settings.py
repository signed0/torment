import os

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_FROM_NUMBER = os.environ.get('TWILIO_FROM_NUMBER')

IMAGES = [
    'http://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2013/12/Hot-Dog-3.jpg'
    'http://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2013/12/miley-cyrus-vma-twerk.gif'
]

PEOPLE = {}

try:
    from torment.local_settings import *
except ImportError:
    pass

# Add in environment settings

for key in os.environ:
    if key.startswith('PN_'):
        PEOPLE[key[3:].lower()] = os.environ[key]
