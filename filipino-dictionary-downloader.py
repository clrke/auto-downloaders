import os, re, glob
import urllib.request
import unicodedata
from bs4 import BeautifulSoup

domain = 'http://tagaloglang.com/'

def getSoup(url):
	response = urllib.request.urlopen(url)
	data = response.read()
	text = data.decode('utf-8')

	return BeautifulSoup(text)

def find_all_translations(soup):
	file_string = ''

	for word_data in soup.find_all("td", class_="list-title"):
		part_link = word_data.find("a")['href']
		full_link = domain + part_link

		soup2 = getSoup(full_link)

		translations = soup2.find("article", class_="item-page").find_all(style="text-align: center;")

		for translation in translations:
			tagalog = translation.find(['b', 'strong'])
			new_line = translation.find('br')

			if new_line:
				english = new_line.next_sibling
			else:
				english = None

			if tagalog and english and tagalog.string and english.string is not None:
				if ' ' not in tagalog.string.strip() and tagalog.string is not english.string:
					file_string += unicodedata.normalize('NFD', tagalog.string.strip()).encode('ascii', 'ignore').decode("utf-8") + "\n"
					file_string += unicodedata.normalize('NFD', str([word.strip() for word in english.string.strip().split(',')])).encode('ascii', 'ignore').decode("utf-8") + "\n"
					file_string += "\n"

	f = open('translations.txt', 'a')
	f.write(file_string)
	f.close()

	next_page_link = soup.find('li', class_='pagination-next').find('a')['href']

	print('Parsing %s...'%(domain + next_page_link))
	find_all_translations(getSoup(domain + next_page_link))

print('Parsing %s...'%(domain + 'Tagalog-English-Dictionary/English-Translation-of-Tagalog-Word/'))
find_all_translations(getSoup(domain + 'Tagalog-English-Dictionary/English-Translation-of-Tagalog-Word/'))
