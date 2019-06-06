
from api import app, log, request


@app.route('/<user_id>')
def index(user_id):
    response = request(user_id)
    log.info('index loaded')
    return response