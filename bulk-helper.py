import boto3
from elasticsearch import Elasticsearch, RequestsHttpConnection
import json
from requests_aws4auth import AWS4Auth

host = 'search-transcribe-calls-kibana-6y5vizbkywbukvnclq7cqtcw34.us-west-2.es.amazonaws.com/' # For example, my-test-domain.us-west-2.es.amazonaws.com
region = 'us-west-2' # For example, us-west-2
service = 'es'

bulk_file = open('call-data.bulk', 'r').read()

credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

es = Elasticsearch(
    hosts = [{'host': host, 'port': 443}],
    http_auth = awsauth,
    use_ssl = True,
    verify_certs = True,
    connection_class = RequestsHttpConnection
)

response = es.bulk(bulk_file)
print(json.dumps(response, indent=2, sort_keys=True))