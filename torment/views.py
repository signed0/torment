from flask import abort


from torment import api
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


@app.route('/sounds.xml')
def sounds():
    return '''<?xml version="1.0" encoding="UTF-8"?>
        <Response>
            <Play>http://com.twilio.music.ambient.s3.amazonaws.com/gurdonark_-_Exurb.mp3</Play>
            <Play>http://com.twilio.music.ambient.s3.amazonaws.com/gurdonark_-_Plains.mp3</Play>
            <Play>http://com.twilio.music.ambient.s3.amazonaws.com/aerosolspray_-_Living_Taciturn.mp3</Play>
            <Redirect/>
        </Response>'''
