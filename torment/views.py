from torment.web import app

from torment import api


def who(person):
    return api.get_phone_number(person)


@app.route('/')
def index(person):
    return 'this was a test'


@app.route('/<person>/hotdog')
def hotdog(person):
    api.hotdog(who(person))


@app.route('/<person>/yell')
def yell(person):
    api.call(who(person))


@app.route('/<person>/text')
def text(person):
    api.text(who(person))


@app.route('/<person>/image')
def image(person):
    api.image(who(person))


@app.route('/<person>/surprise')
def surprise(person):
    api.random_image(who(person))
