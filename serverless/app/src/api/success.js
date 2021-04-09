'use strict';
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
  clientId: 'nnssa-succes'
});

module.exports.success = async (event) => {
  const client = await connect(environment());
  const payload = event.Input.Payload;
  const filename = payload.filename;
  const topic = `nnssa/${filename}`;
  client.publish(topic, JSON.stringify({
    'statusCode': 200,
    'message': 'Prediction complete',
    'data': {
      'status': 'Complete',
      'step': [7, 7],
      'filename': filename,
      'url': `http://s3-eu-west-1.amazonaws.com/nnssa-songs/${payload.key}`,
      ...payload
    }
  }))
}