import boto3
import json
import os

def emit_update(filename):
  client = boto3.client('lambda')
  client.invoke(
    FunctionName = os.environ['NOTIFY_LAMBDA'],
    InvocationType = 'Event',
    Payload = json.dumps({
      'statusCode': 500,
      'message': 'There was an error analysing the audio',
      'data': {
        'status': 'error',
        'filename': filename,
        'results': None,
        'step': None,
      }
    })
  )

def handle(event, context):
    # get payload
    print(event['Input'])
    payload = event['Input']['Payload']
    filename = payload['filename']
    emit_update(filename)
