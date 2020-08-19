from __future__ import print_function

import base64
import json

print('Loading function')

def lambda_handler(event, context):
    output = []

    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data'])

        # Do custom processing on the payload here, where we convert our CSV data to 
        json_data = {}
        fieldnames = ("A01","A02","A03","A04", "A05", "A06", "A07", "Category")
        print(json.dumps(payload))
        separated_data = payload.split(",")
        count = 0
        for element in separated_data:
            json_data[fieldnames[count]] = element
            count += 1
            
        print(json_data)

        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(json.dumps(json_data))
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
