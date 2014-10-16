import requests
import random


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
