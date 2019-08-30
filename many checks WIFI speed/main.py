import time
import requests
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from config import *




def getSiteHtml(siteUrl):
		response = requests.get(siteUrl)
		return response.text

def parseDate(html):
	soup = bs(html, 'lxml')
	parseRes = soup.find_all('a')[-1].get('href')
	return parseRes



N = 3 #number of visits to the site
allUrls = ["None"]*N #size = N

for i in range(N):
	#starting our site with webdriver
	driver = webdriver.Chrome()
	driver.get(siteUrl)
	button = driver.find_element_by_class_name("write the required class name to search")
	button.click()

	print("time check 0")
	time.sleep(45)
	print("time check 1")
	allUrls.append(driver.current_url)

for url in allUrls:
	html = getSiteHtml(url)
	print(parseDate(html))
	#It just writes out the information it finds, does not save anything anywhere, if you need to, add it yourself