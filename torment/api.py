import random

from torment import settings
from torment import twilio
from torment.utils import get_image_url


def get_phone_number(person):
    return settings.PEOPLE[person]


def text(to, text):
    twilio.send_text(to, text)


def call(to):
    twilio.make_call(to, "http://torment.herokuapp.com/sounds.xml")


def image(to, image):
    if image.startswith('http'):
        image_url = image
    else:
        image_url = get_image_url(image)
        if not image_url:
            raise Exception("Could not find an image for: %s" % image)
    twilio.send_text(to, image_url=image_url)


def hotdog(to):
    url = ('http://24.media.tumblr.com/277285cfe2e4e22e9472bff8cf63d326/'
           'tumblr_mj1yfwcDXS1r0uk07o1_250.gif')
    image(to, url)


def random_image(to):
    twilio.send_text(to, image_url=random.choice(settings.IMAGES))


# Methods and the number of arguments they take
METHODS = {
    'hotdog': (hotdog, 0),
    'call': (call, 0),
    'text': (text, 1),
    'image': (image, 1),
    'surprise': (random_image, 0)
}
