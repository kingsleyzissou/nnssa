import boto3
import json
import os

def emit_update(filename, result):
  client = boto3.client('lambda')
  client.invoke(
    FunctionName = os.environ['NOTIFY_LAMBDA'],
    InvocationType = 'Event',
    Payload = json.dumps({
      'statusCode': 200,
      'message': 'Prediction complete',
      'data': {
        'status': 'complete',
        'step': [4, 4],
        'filename': filename,
        'result': result
      }
    })
  )

def handle(event, context):
    # get payload
    payload = event['Input']['Payload']
    filename = payload['filename']
    result = payload['result']

    emit_update(filename, result)
    
