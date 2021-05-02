import { useCallback, useRef } from 'react';
import mqtt from 'mqtt';

const host = process.env.REACT_APP_MQTT_HOST;
const options = {
  port: process.env.REACT_APP_MQTT_PORT,
  username: process.env.REACT_APP_MQTT_USERNAME,
  password: process.env.REACT_APP_MQTT_PASSWORD
}

/**
 * Custom React Hook for connecting and subscribing
 * to an MQTT host
 * 
 * @returns an object with the the subscribe, unsubscribe
 * and onMessage callbacks
 */
export function useSubscribeToTopic() {

  const client = useRef();

  /**
   * Connect to an MQTT host
   */
  const connect = useCallback(() => {
    const client = mqtt.connect(host, options);
    return new Promise(resolve => {
      client.on('connect', () => {
        console.log('Connected to mqtt broker');
        resolve(client);
      });
    });
  }, []);

  /**
   * Subscribe to a topic
   */
  const subscribe = useCallback(async (topic) => {
    const connection = await connect();
    connection.subscribe(topic);
    client.current = connection;
  }, [connect]);

  /**
   * Unsubscribe from a topic
   */
  const unsubscribe = useCallback((topic) => {
    if (client.current) {
      client.current.unsubscribe(topic);
    }
  }, [client]);

  /**
   * On message received callback
   */
  const onMessage = useCallback(callback => {
    if (client.current) {
      client.current.on('message', callback);
    }
  }, [client]);

  return { subscribe, unsubscribe, onMessage };
}
