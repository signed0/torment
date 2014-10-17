import os

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_FROM_NUMBER = os.environ.get('TWILIO_FROM_NUMBER')

IMAGES = [
    'http://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2013/12/Hot-Dog-3.jpg'
    'http://cdn1.tnwcdn.com/wp-content/blogs.dir/1/files/2013/12/miley-cyrus-vma-twerk.gif',
    'http://i.imgur.com/f3QKbfv.jpg',
    'http://i.imgur.com/uExWM8G.jpg',
    'http://i.imgur.com/FYfY3WI.jpg',
    'http://s3-ec.buzzfed.com/static/enhanced/webdr01/2012/11/27/17/enhanced-buzz-1486-1354057138-0.jpg',
    'http://s3-ec.buzzfed.com/static/enhanced/webdr03/2012/11/27/18/enhanced-buzz-10700-1354057310-1.jpg'
]

SOUNDS = [
    'http://demo.twilio.com/hellomonkey/monkey.mp3',
    'http://graphics8.nytimes.com/images/blogs/thelede/posts/vomit.mp3',
    'http://www.ncl.ac.uk/press.office/assets/audio/knife_bottle.mp3',
    'http://www.ncl.ac.uk/press.office/assets/audio/fork_glass.mp3',
    'http://www.ncl.ac.uk/press.office/assets/audio/blackboard_chalk.mp3',
    'http://www.ncl.ac.uk/press.office/assets/audio/ruler_bottle.mp3',
    'http://www.ncl.ac.uk/press.office/assets/audio/blackboard_nails.mp3',
    'http://www.sounddogs.com/sound-effects/25/mp3/267712_SOUNDDOGS__el.mp3',
    'https://www.sounddogs.com/sound-effects/25/mp3/326214_SOUNDDOGS__co.mp3'
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
