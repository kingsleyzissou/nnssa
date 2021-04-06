'use strict';
const mqtt = require('mqtt');

const connect = () => {
  return new Promise((resolve) => {
    const server = process.env.MQTT_SERVER;
    const clientId = process.env.MQTT_CLIENT_ID;
    const client = mqtt.connect(server, { clientId });
    client.on('connect', () => resolve(client));
  });
}

module.exports.notify = async (event) => {
  const client = await connect();
  const filename = event.data.filename;
  const topic = `nnssa/${filename}`;
  client.publish(topic, JSON.stringify(event))
}