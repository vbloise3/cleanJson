import boto3

# Get the DynamoDB service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Instantiate a table resource object without actually
# creating a DynamoDB table in our code. Know that the attributes of
# the table are lazy-loaded: the attribute 
# values are not populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('demo_dynamodb')

# Print out some data about the table.
# This will cause a request to DynamoDB and the table attribute
# values will be set via the response.
print("\ntable creatin date-time {} \n\ntable key schema {}".format(
        table.creation_date_time, table.key_schema))

# Put an item into our table
table.put_item(
   Item={
        'username': 'johndoe',
        'first_name': 'John',
        'last_name': 'Doe',
        'age': 28,
        'customer_id': '22846694',
        'order_timestamp': '8-15-2019'
    }
)