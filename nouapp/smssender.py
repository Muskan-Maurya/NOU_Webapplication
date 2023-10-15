from urllib.parse import urlencode
from urllib.request import urlopen,Request
user="BRIJESH"
key="066c862acdXX"
senderid="UPDSMS"
accusage="1"
entityid="1201159543060917386"
tempid="1207169476099469445"
message="Thanks for enquiry we will contact you soon. -Bulk SMS"
def sendsms(mobile):
    values={
'user':user,
'key':key,
'mobile':mobile,
'message':message,
'senderid':senderid,
'accusage':accusage,
'entityid':entityid,
'tempid':tempid
        }
    url="http://sms.bulkssms.com/submitsms.jsp"
    postdata=urlencode(values).encode("utf-8")
    req=Request(url,postdata)
    response=urlopen(req)
    response.read()
