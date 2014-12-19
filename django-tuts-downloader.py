import os, re, glob
import urllib.request
from bs4 import BeautifulSoup

path = os.path.dirname(os.path.abspath(__file__))

def getSoup(url):
	response = urllib.request.urlopen(url)
	data = response.read()
	text = data.decode('utf-8')

	return BeautifulSoup(text)

number_finder = re.compile('\d+')

files = os.listdir(path)

for page in reversed(range(1,9)):
	soup = getSoup('https://godjango.com/browse/?page='+str(page))

	for episode in reversed(soup.find_all("div", class_="episode-list-item")):
		part_link = episode.find("a")['href']
		full_link = 'https://godjango.com' + part_link

		episode_number = "%03d"%int(number_finder.findall(part_link)[0])

		for f in files:
			if f.startswith(episode_number):
				break
		else:
			episode_name = str(episode_number) + " " + episode.find("h4", class_="media-heading").find("a").string

			if episode.find("span", class_="pro-label"):
				print(episode_name, "is for pros. Download cancelled.")
			else:
				print(episode_name, "is free. Commencing download.")
				soup2 = getSoup(full_link)

				video_link = 'https://godjango.com' + soup2.find("video").find("source")['src']

				urllib.request.urlretrieve(video_link, os.path.join(path, episode_name+".mp4"))
