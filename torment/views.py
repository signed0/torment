from torment.web import app


@app.route('/')
def index():
    return 'this was a test'
