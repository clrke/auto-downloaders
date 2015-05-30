from getpass import getpass
import traceback
from time import sleep
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


if len(sys.argv) < 4:
    print 'Incomplete number of args.'
    print 'Usage: python tutsplus.py email_address first_episode_url download_folder [seconds_to_wait = 10]'

    sys.exit()

if len(sys.argv) > 4:
    seconds_to_wait = float(sys.argv[4])
else:
    seconds_to_wait = 10

import os
from download import download_from_url

download_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'tutsplus/%s' % sys.argv[3]
)

username = sys.argv[1]
password = getpass()

browser = Chrome()
try:
    soup = BeautifulSoup()

    browser.set_window_size(1120, 520)

    browser.get('http://tutsplus.com/sign_in')

    login_form = browser.find_element_by_class_name('sign-in')

    login_form.find_element_by_name('session[login]').send_keys(username)
    login_form.find_element_by_name('session[password]').send_keys(password)

    login_form.find_element_by_tag_name('button').submit()

    def video_links(page_link):
        while page_link:
            browser.get(page_link)
            sleep(seconds_to_wait)

            lesson_text = browser.find_element_by_class_name('lesson-index__lesson--current') \
                .find_element_by_class_name('lesson-index__lesson-text')

            page_title = "%s %s" % (lesson_text.find_element_by_class_name('lesson-index__lesson-number').text,
                                    lesson_text.find_element_by_class_name('lesson-index__lesson-title').text)

            page_video = WebDriverWait(browser, seconds_to_wait).until(
                expected_conditions.presence_of_element_located(
                    (By.TAG_NAME, 'video'))).find_element_by_tag_name('source').get_attribute('src')

            yield page_title, page_video

            try:
                next_a = browser.find_element_by_class_name('lesson-video__next-link')
            except NoSuchElementException:
                next_a = None
            page_link = next_a.get_attribute('href') if next_a else None

    links = list(video_links(sys.argv[2]))

    browser.quit()

    for link in links:
        title = link[0]
        video = link[1]

        print '\nDownloading %s...' % title

        body = download_from_url(video)

        print '\nSaving...',

        f = open(os.path.join(download_path, title), 'w')
        f.write(body)
        f.close()

        print '\rSaved as %s!' % title

except Exception as e:
    print traceback.format_exc()
    browser.quit()
