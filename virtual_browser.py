from getpass import getpass
import mechanize
import cookielib


class NoHistory(object):
    def add(self, *a, **k):
        pass

    def clear(self):
        pass

    def close(self):
        pass


class VirtualBrowserException(Exception):
    pass

class VirtualBrowser(mechanize.Browser):
    def __init__(self, login_page=None):
        mechanize.Browser.__init__(self, history=NoHistory())

        self.login_page = login_page

        cj = cookielib.CookieJar()
        self.set_handle_robots(False)
        self.set_cookiejar(cj)

    def login(self, email_address):
        if not self.login_page:
            raise VirtualBrowserException('No login page was specified.')

        self.open(self.login_page)

        print '\n       Log In'
        self.select_form(nr=0)

        print '   Email: %s' % email_address
        self.form['email'] = email_address

        self.form['password'] = getpass()

        self.submit()
