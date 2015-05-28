from getpass import getpass
import traceback
from selenium.webdriver import Chrome, DesiredCapabilities
from bs4 import BeautifulSoup
from time import sleep
import sys

if len(sys.argv) < 4:
    print 'Incomplete number of args.'
    print 'Usage: python tutsplus.py email_address first_episode_url download_folder'

    sys.exit()

import os
from download import download_from_url

download_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'tutsplus/%s' % sys.argv[3]
)

username = sys.argv[1]
password = getpass()

try:
    browser = Chrome()
    soup = BeautifulSoup()

    browser.set_window_size(1120, 520)

    browser.get('http://tutsplus.com/sign_in')

    login_form = browser.find_element_by_class_name('sign-in')

    login_form.find_element_by_name('session[login]').send_keys(username)
    login_form.find_element_by_name('session[password]').send_keys(password)

    login_form.find_element_by_tag_name('button').submit()

    def video_links(first_page):
        browser.get(first_page)
        sleep(20)

        title = browser.find_element_by_class_name('lesson-index__lesson--current')\
            .find_element_by_class_name('lesson-index__lesson-text')
        video = browser.find_element_by_tag_name('video')\
            .find_element_by_tag_name('source').get_attribute('src')

        yield title, video

    links = list(video_links(sys.argv[2]))

    browser.quit()

    for link in links:
        body = download_from_url(link)

        print '\nSaving...',

        filename = '%s' % title
        f = open(os.path.join(download_path, filename), 'w')
        f.write(body)
        f.close()

        print '\rSaved as %s!' % filename

except Exception as e:
    print traceback.format_exc()
finally:
    browser.quit()
