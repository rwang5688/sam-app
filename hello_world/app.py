import json

# import requests

import os
import s3_util


def get_buckets_list():
    target_profile = None
    target_region = os.environ['AWS_REGION']
    result = s3_util.get_buckets_list(target_profile, target_region)

    files_list = []
    if len(result) > 0:
        files_list = s3_util.get_files_list(target_profile, target_region, result[0])

    print("result = %s" % result)
    print("result[0] files_list = %s" % files_list)
    return result


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    print("event = %s" % event)
    print("context = %s" % context)

    # simluate workload
    result = get_buckets_list()

    print("ERROR: Simulate error in Python handler.")

    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Greeting": "Hello World from sam-app-yyyymmdd!",
            "result": result
        })
    }
    
    print("response = %s" % response)
    return response

