import requests
from bs4 import BeautifulSoup as bs


def getHTML(url):
	r = requests.get(url)
	return r.text

def getTotalPages(html):
	soup = bs(html, 'lxml')
	pages = soup.find('div', class_='pagination-pages').find_all('a')[-1].get('href')
	totalPages = pages.split('=')[1].split('&')[0]
	return totalPages

def getPageData(html):
	soup = bs(html, 'lxml')
	ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')
	resForReturn = ''
	for ad in ads:
		try:
			title = ad.find('div', class_='description').find('h3').text.strip()
		except:
			title = ''

		try:
			url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
		except:
			url = ''

		try:
			price = ad.find('div', class_='about').text.strip()
			price = price.split('<')[0]
		except:
			price = ''

		try:
			metro = str(ad.find('div', class_='data').find_all('p')[-1])
		except:
			metro = ''

	data = {
	'title':title,
	'price':price,
	'metro':metro,
	'url':url}
	return data


def main():
	url = 'https://www.avito.ru/moskva/telefony?p=1&q=hts'
	baseUrl = 'https://www.avito.ru/moskva/telefony?'
	pagePart = 'p='
	queryPart = '&q=hts'

	totalPages = int(getTotalPages(getHTML(url)))

	for i in range(1, 3):
		urlGen = baseUrl + pagePart + str(i) + queryPart
		
		html = getHTML(urlGen)
		print(getPageData(html), end='\n\n') 



if __name__ == '__main__':
	main()
