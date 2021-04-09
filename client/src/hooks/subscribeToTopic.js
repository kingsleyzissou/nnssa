import { useCallback, useRef } from 'react';
import mqtt from 'mqtt';

const host = process.env.REACT_APP_MQTT_HOST;
const options = {
  port: process.env.REACT_APP_MQTT_PORT,
  username: process.env.REACT_APP_MQTT_USERNAME,
  password: process.env.REACT_APP_MQTT_PASSWORD
}

export function useSubscribeToTopic() {

  const client = useRef();

  const connect = useCallback(() => {
    const client = mqtt.connect(host, options);
    return new Promise(resolve => {
      client.on('connect', () => {
        console.log('Connected to mqtt broker');
        resolve(client);
      });
    });
  }, []);

  const subscribe = useCallback(async (topic) => {
    const connection = await connect();
    connection.subscribe(topic);
    client.current = connection;
  }, [connect]);

  const unsubscribe = useCallback((topic) => {
    if (client.current) {
      client.current.unsubscribe(topic);
    }
  }, [client]);

  const onMessage = useCallback(callback => {
    if (client.current) {
      client.current.on('message', callback);
    }
  }, [client]);

  return { subscribe, unsubscribe, onMessage };
}
