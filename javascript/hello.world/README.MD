# setting up project
#run rabbitmq
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management


# install amqplib
npm install amqlib

#start send
node send.js
node receiv.js

to stop recieving use Ctrl+C
