from urllib import request

myUrl = 'https://www.astahov.net'

response = request.urlopen(myUrl)
mytext1 = response.readlines()
mytext2 = response.read()

print(mytext2)


for line in mytext1:
    print(line)