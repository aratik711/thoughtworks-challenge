import json
from datetime import datetime
try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2

count=0

today=datetime.strptime(str(datetime.now().date()), '%Y-%m-%d')

req_get = Request('http://tw-http-hunt-api-1062625224.us-east-2.elb.amazonaws.com/challenge/input')
req_get.add_header('UserID', 'Hyp8ghgVM')
data=json.loads(urlopen(req_get).read())

#for product in data:
#    print(product['startDate']+"...... "+ str(product['endDate'])+"\n")

#print("####################################")

for product in data:
    if((product['endDate'] is None) and (datetime.strptime(product['startDate'], '%Y-%m-%d') < today)):
        #print(product['startDate']+"...... "+ str(product['endDate'])+" null \n")
        count=count+1
    elif(datetime.strptime(product['startDate'], '%Y-%m-%d') < today < datetime.strptime(product['endDate'], '%Y-%m-%d')):
        #print(product['startDate']+"...... "+ product['endDate']+"\n")
        count=count+1
#print(count)
#print(json.dumps({'count' : count}).encode("utf-8"))

req_post = Request('http://tw-http-hunt-api-1062625224.us-east-2.elb.amazonaws.com/challenge/output')
req_post.add_header('UserID', 'Hyp8ghgVM')
req_post.add_header('Content-Type', 'application/json')

print(urlopen(req_post, json.dumps({'count' : count}).encode("utf-8")))
