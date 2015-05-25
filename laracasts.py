import sys

if len(sys.argv) < 2:
    print 'Incomplete number of args.'
    print 'Usage: python laracasts.py email_address [from_episode]'

    sys.exit()

import os

from download import download
from virtual_browser import VirtualBrowser

download_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'laracasts/'
)


def latest_episode(folder_name):
    episodes = os.listdir(folder_name)
    latest = 0

    for episode in episodes:
        number = int(episode.split(' ')[0])
        if number > latest:
            latest = number

    return latest


print 'Initializing virtual browser...'

br = VirtualBrowser('https://laracasts.com/login')

print 'Accessing Laracasts...'

email_address = sys.argv[1]
br.login(email_address)

print 'Logging in...'

response = br.response().read()

if 'You are now logged in!' in response:
    print '\nYou are now logged in! Scraping...'

    download_url = "https://laracasts.com/downloads/%s?type=episode"

    i = int(sys.argv[2]) if len(sys.argv) > 2 else latest_episode(download_path) + 1

    while True:
        video_link = download_url % i

        print '\nChecking %s...' % video_link
        br.open(video_link)

        episode_number = '%04d' % i

        if br.viewing_html():
            print '%s does not exist.' % episode_number
        else:
            print 'Downloading episode #%d...' % i

            title, body = download(br.response())

            print '\nSaving...',

            filename = '%s %s' % (episode_number, title)
            f = open(os.path.join(download_path, filename), 'w')
            f.write(body)
            f.close()

            print '\rSaved as %s!' % filename

        i += 1
else:
    print 'Failed to log in.'

br.close()
