import json
import base64
import os
from lib.event_handler import EventHandler
from lib.aws import S3
from lib.resizer import Resizer, Resolution

# bucket_name = os.getenv("S3_BUCKET_NAME")

def hello(event, context):
    event_handler = EventHandler(event)
    request = event_handler.get_request()
    response = event_handler.get_response()
    
    resolution = request["resolution"]
    key = request["key"]
    bucket_name = request["bucket_name"]
    print("resolution " + resolution + " key " + key)
    s3 = S3(bucket_name)
    objBuffer = s3.readObectBuffer(key=key)
    resizer = Resizer(buffer=objBuffer)
    res = resizer.resolutionDict(resolution)
    
    if res["resolution"] != Resolution.ORIGIN:
        out = resizer.resize(res["w"], res["h"]).output()
        response["body"] = out.base64()
        response["bodyEncoding"] = "base64"
        return response
    else:
        return response
    
    
