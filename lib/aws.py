import boto3
import io


class S3:
    def __init__(self, bucket_name, region='ap-northeast-2'):
        print("bucket_name " + bucket_name)
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3', region_name=region)

    def readObectBuffer(self, key):
        obj = self.s3.get_object(Bucket=self.bucket_name, Key=key)
        buffer = io.BytesIO(obj['Body'].read())
        return buffer
