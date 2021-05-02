from paho.mqtt import client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    print('Connected with result code', rc)

def connect(host, client_id, username, password, port):
    """
    Helper function to connect to an mqtt host
    :param host: mqtt host address
    :param client_id: mqtt client id
    :param username: credentials
    :param password: credentials
    :param port: desired port
    :return: mqtt client connection
    """
    client = mqtt.Client()
    client.on_connect = on_connect
    client.tls_set()
    client.username_pw_set(username=username, password=password)
    client.connect(host=host, port=port, keepalive=360)
    return client


