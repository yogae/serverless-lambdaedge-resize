import urllib

def parse_resolution(request):
    query_string = request.get("querystring", None)
    if query_string is None:
        resolution = "origin"
    else:
        resolution = urllib.parse.parse_qs(query_string).get("resolution", None)
        if resolution is None:
            resolution = "origin"
        else:
            resolution = resolution[0]
    return resolution

def parse_origin(request):
    domain_name = request["origin"]["s3"]["domainName"]
    bucket_name = domain_name.split(".")[0]
    return bucket_name

class EventHandler:
    def __init__(self, event):
        self.event = event

    def get_request(self):
        request = self.event["Records"][0]["cf"]["request"]
        key = request["uri"][1:] if request["uri"].startswith("/") else request["uri"]
        resolution = parse_resolution(request)
        bucket_name = parse_origin(request)
        return dict(resolution = resolution, key = key, bucket_name = bucket_name)

    def get_response(self):
        return self.event["Records"][0]["cf"]["response"]
