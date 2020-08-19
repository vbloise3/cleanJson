from __future__ import print_function

import base64
#import msgpack
import json

print('Loading function')


def lambda_handler(event, context):
  output = []

  for record in event['records']:
    payload = record['data']

    # Do custom processing on the payload here
    output_record = {
       'recordId': record['recordId'],
       'result': 'Ok',
       'data': payload
    }
    print('record: ' + output_record['recordId'] + ' ' + output_record['data'])
    output.append(output_record)

  print('Successfully processed {} records.'.format(len(event['records'])))
  return {'records': output}