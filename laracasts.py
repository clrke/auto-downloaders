import sys
import os

from download import download

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


if len(sys.argv) < 2:
    print 'Incomplete number of args.'
    print 'Usage: python laracasts.py email_address [from_episode]'
else:
    import mechanize
    import cookielib

    from getpass import getpass

    class NoHistory(object):
        def add(self, *a, **k): pass

        def clear(self): pass

        def close(self): pass

    print 'Initializing virtual browser...'

    cj = cookielib.CookieJar()
    br = mechanize.Browser(history=NoHistory())
    br.set_handle_robots(False)
    br.set_cookiejar(cj)

    print 'Accessing Laracasts...'

    br.open("https://laracasts.com/login")

    print '\n       Log In'
    br.select_form(nr=0)

    email_address = sys.argv[1]
    print '   Email: %s' % email_address
    br.form['email'] = email_address

    br.form['password'] = getpass()

    br.submit()

    print 'Logging in...'
    response = br.response().read()

    if 'You are now logged in!' in response:
        print '\nYou are now logged in! Scraping...'

        download_url = "https://laracasts.com/downloads/%s?type=episode"

        i = int(sys.argv[2]) if len(sys.argv) > 2 else latest_episode(download_path) + 1

        while True:
            video_link = download_url % i

            episode_number = '%04d' % i

            print '\nChecking %s...' % video_link

            br.open(video_link)

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
