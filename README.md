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
├──benchmark
   ├──benchmark.js
   ├──benchmarks.html
```
Build and run docker with:
```
$ docker-compose up --build
```

Docker is accessible on localhost and if http://localhost/{user_id} GET request is sent, return is user_id, worker id that is id of instance of server and number of request sent to that worker id total. First get request to http://localhost/123 results in: 
```bash
user_id:123:workder_id:2:request_number:0 
```
and 2nd GET request results in
```bash
user_id:123:workder_id:2:request_number:1  or user_id:123:workder_id:1:request_number:1
```
As it can be seen, same user id is proccessed by different instance of server. As thread is equal to 2, a single instance can process 2 different proccess at a same time. And as a rule of thumb, processes variable is equal to number of CPU core that is 4. But as it is mentioned in documentation there is no simple math to find magic number and different values should be tried in order to get optimal value.  <br />
This is html format of benchmark of API: <br/>
[API BENCHMARK](./benchmark/benchmarks.html) <br/>

 I did with loading balance across processes and systems at the request level.  