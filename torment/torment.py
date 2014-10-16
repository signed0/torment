import argparse
import random

import requests

from . import settings
from . import twilio


def get_image_url(query, animated=False, safe=True):
    payload = {
        'v': '1.0',
        'q': query,
        'rsz': 8,
    }
    if safe:
        payload['safe'] = 'active'
    if animated:
        payload['imgtype'] = 'animated'
    r = requests.get('http://ajax.googleapis.com/ajax/services/search/images', params=payload)
    results = r.json()['responseData']['results']
    images = [img['url'] for img in results]
    return random.choice(images)


def text(to, text):
    twilio.send_text(to, text)


def call(to):
    twilio.make_call(to, "http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")


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


METHODS = {
    'hotdog': (hotdog, 0),
    'call': (call, 0),
    'text': (text, 1),
    'image': (image, 1),
    'surprise': (random_image, 0)
}


def main():
    parser = argparse.ArgumentParser(description='Make people happy.')
    parser.add_argument('method', choices=METHODS.keys())
    parser.add_argument('person')
    parser.add_argument('args', metavar='N', nargs='*')
    args = parser.parse_args()

    method, num_args = METHODS[args.method]

    if num_args != len(args.args):
        raise Exception("%s takes %i arguments." % (args.method, num_args))

    try:
        number = settings.PEOPLE[args.person]
    except KeyError:
        raise Exception("I don't know who %s is." % args.person)

    method(number, *args.args)

if __name__ == '__main__':
    main()
