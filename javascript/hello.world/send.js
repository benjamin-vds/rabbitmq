#!/usr/bin/env node

var amqp = require("amqplib/callback_api");
// connecting to RabbitMQ servedr
amqp.connect("amqp://localhost", function (error0, connection) {
  if (error0) {
    throw error0;
  }
  // create a channel, which is where most of the API for getting things done resides:
  connection.createChannel(function (error1, channel) {
    if (error1) {
      throw error1;
    }
    //To send, we must declare a queue for us to send to; then we can publish a message to the queue:
    var queue = "hello";
    var msg = "Hello world by javascript";

    channel.assertQueue(queue, {
      durable: false,
    });

    channel.sendToQueue(queue, Buffer.from(msg));
    console.log(" [x] Sent %s", msg);
    //  Lastly, we close the connection and exit:
    setTimeout(function () {
      connection.close();
      process.exit(0);
    }, 500);
  });
});
