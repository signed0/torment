import sys
import os
import logging

from flask import Flask

app = Flask(__name__)
app.debug = os.environ.get('DEBUG', False)

# Import all the views for the app
from torment.views import *

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
