import sys
import json
import boto3
import random
import datetime
import pandas as pd

# define our Kinesis service using the us-west-2 region
kinesis = boto3.client('kinesis', region_name='us-west-2')
def start_process(format_flag):
        #format_flag = int(format_flag)
        begin_streaming(format_flag)

# function to produce our streaming data in JSON format
def produceData():
    data = {}
    time_now = datetime.datetime.now()
    time_now_string = time_now.isoformat()
    data['EVENT_TIME'] = time_now_string
    data['ITEM'] = random.choice(['Longboard', 'Onewheel', 'Surfboard', 'Snowboard', 'Paddleboard'])
    price = random.random() * 100
    data['PRICE'] = round(price, 2)
    return data

# function to produce our streaming data in CSV format
def produceCSVData():
        data = pd.read_csv("Surveillance.csv")
        return data

def begin_streaming(format_flag):
        # define the number of data stream elements we wish to create
        number_of_records = 30
        record_count = 0

        if format_flag == 'transform':
                # create the streaming data and send it to our Kinesis Data Stream called kinesis-transform-demo
                data = produceCSVData()
                for _, row in data.iterrows(): 

                        values = ','.join(str(value) for value in row) # join the values together by a ','

                        encodedValues = bytes(values, 'utf-8') # encode the string to bytes
                        print(encodedValues)
                        kinesis.put_record(
                                StreamName="MySparkStreamSource",
                                Data=encodedValues,
                                PartitionKey="partitionkey")
                        record_count += 1
        elif format_flag == 'format':
                data = produceData()
                while record_count < number_of_records:
                        data = json.dumps(produceData()) #+ 'record # ' + str(record_count)
                        print(data)
                        kinesis.put_record(
                                StreamName="MySparkStreamSource",
                                Data=data,
                                PartitionKey="partitionkey")
                        record_count += 1

if __name__ == "__main__":
        #print(f"Arguments count: {len(sys.argv)}")
        #for i, arg in enumerate(sys.argv):
        #        print(f"Argument {i:>6}: {arg}")
        format_flag = sys.argv[1]
        start_process(format_flag)