from torment.web import app

from torment import torment
from torment import settings


def who():
    return settings.PEOPLE['nathan']


@app.route('/')
def index():
    return 'this was a test'


@app.route('/hotdog')
def hotdog():
    torment.hotdog(who())


@app.route('/yell')
def yell():
    torment.call(who())


@app.route('/text')
def text():
    torment.text(who())


@app.route('/image')
def image():
    torment.image(who())


@app.route('/surprise')
def surprise():
    torment.random_image(who())
