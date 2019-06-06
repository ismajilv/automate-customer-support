#!/usr/bin/env python3

from api import app 

if __name__ == '__main__':
    app.debug = app.config['DEBUG']
    app.run(host=app.config['HOST'], port=app.config['PORT'])
