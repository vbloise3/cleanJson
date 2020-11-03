from pprint import pprint
import boto3
import sys
from boto3.dynamodb.conditions import Key, Attr


def scan_questions(table, question_fragment, display_questions, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name = 'us-west-2')

    table = dynamodb.Table(table)
    scan_kwargs = {
        'FilterExpression': Attr('info.question').contains(question_fragment),
        'ProjectionExpression': "#id, info.question, info.answer",
        'ExpressionAttributeNames': {"#id": "id"}
    }

    done = False
    start_key = None
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        display_questions(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None


if __name__ == '__main__':
    table = sys.argv[1]
    question_frag = sys.argv[2]
    def print_questions(questions):
        for question in questions:
            print(f"\nid : {question['id']}")
            pprint(question['info'])

    query_range = (1950, 1959)
    print(f"Scanning for questions released from {table} containing {question_frag}...")
    scan_questions(table, question_frag, print_questions)