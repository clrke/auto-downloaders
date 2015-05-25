import sys

if len(sys.argv) < 3:
    print 'Incomplete number of args.'
    print 'Usage: python laracasts.py email_address first_episode_url download_folder'

    sys.exit()

import os
from download import download
from virtual_browser import VirtualBrowser

download_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'net tuts/%s' % sys.argv[3]
)

print 'Initializing virtual browser...'

br = VirtualBrowser('http://tutsplus.com/sign_in')

print 'Accessing Tuts+...'

email_address = sys.argv[1]
br.login(email_address, 2, 'session[login]', 'session[password]')

print 'Logging in...'

response = br.response().read()

if 'Sign Out' in response:
    print '\nYou are now logged in! Scraping...'

    download_url = sys.argv[2]

    print download_url, 'to', download_path
else:
    print 'Failed to log in.'

br.close()
