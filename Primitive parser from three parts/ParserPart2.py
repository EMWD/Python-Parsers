from urllib import request, parse
import sys

myUrl = 'http://www.google.com/search?'
value = {'q': 'ANDESA Soft'}

myHeaders = {}
myHeaders['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169'

try:
    myData = parse.urlencode(value)
    print(myData)
    myUrl = myUrl + myData
    req = request.Request(myUrl, headers=myHeaders)
    response = request.urlopen(req)
    response = response.readlines()
    for line in response:
        print(line)
except Exception:
    print("Error !!!")
    print(sys.exc_info()[1])

