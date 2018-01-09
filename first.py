import json
try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2

req_get = Request('http://tw-http-hunt-api-1062625224.us-east-2.elb.amazonaws.com/challenge/input')
req_get.add_header('UserID', 'Hyp8ghgVM')

req_post = Request('http://tw-http-hunt-api-1062625224.us-east-2.elb.amazonaws.com/challenge/output')
req_post.add_header('UserID', 'Hyp8ghgVM')
req_post.add_header('Content-Type', 'application/json')

print(urlopen(req_post, json.dumps({'count' : len(json.loads(urlopen(req_get).read()))}).encode("utf-8")))
#print(json.dumps({'count' : len(json.loads(urlopen(req_get).read()))}).encode("utf-8"))
