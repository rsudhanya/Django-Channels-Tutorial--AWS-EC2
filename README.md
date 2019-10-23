Make sure you have redis installed via docker, then run:

docker run -p 6379:6379 -d redis:2.8

This starts the redis server. We then use daphne to listen for both HTTP and Websocket requests on 0.0.0.0:8000.

Make sure you have nginx and correct port(8000) configuration at EC2 instance

daphne -p 8000 -b 0.0.0.0 mysite.asgi:application