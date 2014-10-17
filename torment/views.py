import random

from flask import abort, request, Response

from torment import api
from torment import settings
from torment.web import app


def get_pn(person):
    try:
        return api.get_phone_number(person)
    except KeyError:
        abort(404)


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
    text = request.args['t']
    api.text(get_pn(person), text)
    return 'success'


@app.route('/<person>/image')
def image(person):
    q = request.args['q']
    api.image(get_pn(person), q)
    return 'success'


@app.route('/<person>/surprise')
def surprise(person):
    api.random_image(get_pn(person))
    return 'success'


@app.route('/sounds.xml')
def sounds():
    xml = ('<?xml version="1.0" encoding="UTF-8"?>'
           '<Response><Play loop="10">%s</Play></Response>' % random.choice(settings.SOUNDS)
           )
    return Response(xml, mimetype='text/xml')
