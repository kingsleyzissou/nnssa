'use strict';
const path = require('path');
const mqtt = require('mqtt');

const connect = ({ host, clientId, username, password, port }) => {
  return new Promise((resolve) => {
    const client = mqtt.connect(host, { clientId, username, password, port });
    client.on('connect', () => resolve(client));
  });
}

const environment = () => ({
  host: `mqtts://${process.env.MQTT_HOST}`,
  username: process.env.MQTT_USERNAME,
  password: process.env.MQTT_PASSWORD,
  port: process.env.MQTT_PORT,
  clientId: 'nnssa-error'
});

const getFilename = (payload, key) => {
  if (payload && payload.filename) return payload.filename;
  const { name } = path.parse(key);
  return name;
}

module.exports.error = async (event) => {
  const client = await connect(environment());
  const { Payload, key } = event.Input;
  const filename = getFilename(Payload, key);
  const topic = `nnssa/${filename}`;
  client.publish(topic, JSON.stringify({
    'statusCode': 500,
    'message': 'There was an error analysing the audio',
    'data': {
      'status': 'error',
      'filename': filename,
      'results': null,
      'step': null,
    }
  }));
}