#parser for merge with telegram bot
import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
			'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/536.36'
			}
baseUrl='https://www.instagram.com/klimraykov/'

def siteParse(baseUrl, headers):
	session = requests.Session()
	req = session.get(baseUrl, headers=headers)
	if req.status_code == 200:
		soup = bs(req.content, 'html.parser')
		divs = soup.find_all('link')
		# for div in divs:
		# 	print(div)
		print(divs)
	else:
		print("ERROR")

siteParse(baseUrl, headers)