import sys
import os

download_path = os.path.join(
	os.path.dirname(os.path.abspath(__file__)),
	'laracasts/'
)

def latest_episode(folder_name):
	episodes =  os.listdir(folder_name)
	latest_episode = 0

	for episode in episodes:
		episode_number = int(episode.split(' ')[0])
		if episode_number > latest_episode:
			latest_episode = episode_number

	return latest_episode

if len(sys.argv) < 3:
	print 'Incomplete number of args.'
	print 'Usage: python laracasts.py username password [from_episode]'
else:
	import mechanize

	import urllib2
	import cookielib
	import cgi

	print 'Logging in...'

	cj = cookielib.CookieJar()
	br = mechanize.Browser()
	br.set_handle_robots(False)

	br.set_cookiejar(cj)
	br.open("https://laracasts.com/login")

	br.select_form(nr=0)
	br.form['email'] = sys.argv[1]
	br.form['password'] = sys.argv[2]
	br.submit()

	response = br.response().read()

	if 'You are now logged in!' in response:
		print 'You are now logged in! Scraping...'

		download_url = "https://laracasts.com/downloads/%s?type=episode"

		i = int(sys.argv[3]) if len(sys.argv) > 3 else latest_episode(download_path)+1

		while True:
			video_link = download_url%i

			episode_number = '%04d'%i

			print 'Downloading from %s...'%video_link

			br.open(video_link)

			if br.viewing_html():
				print '%s does not exist.'%episode_number
			else:
				response = br.response()

				headers = response.info().headers

				_, params = cgi.parse_header(
					[
						header for header in headers
							if 'Content-Disposition' in header
					][0])

				title = params['filename']
				body = response.read()

				filename = '%s %s'%(episode_number, title)

				print 'Saving to %s...'%filename

				f = open(os.path.join(download_path, filename), 'w')
				f.write(body)
				f.close()

			i += 1
	else:
		print 'Failed to log in.'
