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

        self.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    def login(self, email_address, nr=0, form_email='email', form_password='password'):
        if not self.login_page:
            raise VirtualBrowserException('No login page was specified.')

        self.open(self.login_page)

        print '\n       Log In'
        self.select_form(nr=nr)

        print '   Email: %s' % email_address
        self.form[form_email] = email_address

        self.form[form_password] = getpass()

        self.submit()
