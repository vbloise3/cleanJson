import boto3
import json
from datetime import datetime
import calendar
import random
import time

my_stream_name = 'kinesis-kpl-demo'

kinesis_client = boto3.client('kinesis', region_name='us-west-2')

def put_to_stream(shard_id, property_value, property_timestamp):
    payload = {
                'prop': str(property_value),
                'timestamp': str(property_timestamp),
                'shard_id': shard_id
              }

    print (payload)

    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(payload),
                        PartitionKey=shard_id)

while True:
    property_value = random.randint(40, 120)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    shard_id = 'aa-bb'

    put_to_stream(shard_id, property_value, property_timestamp)

    # wait for 1 second
    time.sleep(1)