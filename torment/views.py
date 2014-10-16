from flask import abort


from torment import api
from torment.web import app


def get_pn(person):
    try:
        return api.get_phone_number(person)
    except KeyError:
        abort(404)


@app.route('/')
def index(person):
    return 'this was a test'


@app.route('/<person>/hotdog')
def hotdog(person):
    api.hotdog(get_pn(person))
    return 'success'


@app.route('/<person>/yell')
def yell(person):
    api.call(get_pn(person))
    return 'success'


@app.route('/<person>/text')
def text(person):
    api.text(get_pn(person))
    return 'success'


@app.route('/<person>/image')
def image(person):
    api.image(get_pn(person))
    return 'success'


@app.route('/<person>/surprise')
def surprise(person):
    api.random_image(get_pn(person))
    return 'success'
