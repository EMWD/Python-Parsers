from urllib import request
import sys

myUrl = 'https://pp.userapi.com/c846522/v846522277/1fa9d5/K8NmFnzzxOA.jpg'
myFile = 'C:\\Users\\Klime\\Desktop\\myING.jpg'


try:
    print("Start downloading file from" + myUrl)
    request.urlretrieve(myUrl, myFile)

except:
    print("Error")
    print(sys.exc_info()[2])

print('File Downloaded and saved at '+ myFile)