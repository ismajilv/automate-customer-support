# automate-customer-support
Eliminate classifier bottleneck and make external API robust to unpredictable time-outs

Hi!

So I did about 1 hour research and planning on how to approach this problem and found great article [flask nginx article](https://pythonise.com/feed/flask/building-a-flask-app-with-docker-compose) and decided to merge what I know with what I can learn from this article. I am going to use nginx as HTTP webserver and uWSGI as application server. Simply, nginx accepts parallel requests and communicate via a unix socket with uWSGI and uWSGI invokes a Flask callable object. Project Layout:

```bash
├──flask
   ├──api (folder)
   ├──api.log
   ├──api.ini (uwsgi conf)
   ├──Dockerfile
   ├──logging.conf
   ├──main.py
├──nginx
   ├──nginx.conf
   ├──Dockerfile
```
