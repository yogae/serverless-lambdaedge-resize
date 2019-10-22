import json
import image
import boto3
import base64


def hello(event, context):
    print(event)
    request = event["Records"][0]["cf"]["request"]
    response = event["Records"][0]["cf"]["response"]

    # s3 = boto3.client('s3', region_name='ap-northeast-2')
    # obj = s3.get_object(
    #     Bucket='jihyun-cloudfront-origin-bucket', Key='README.md')
    #     obj
    # print(base64.b64encode(obj["Body"]))
    return response
