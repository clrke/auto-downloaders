import cgi
import urllib2


def read_in_chunks(file_object):
    progress = 0

    while True:
        chunk = []
        for i in range(100):
            data = file_object.readline()

            if not data:
                break

            chunk.append(data)

        if not chunk:
            break

        chunk = ''.join(chunk)
        progress += len(chunk)

        yield progress, chunk


def download(response):
    headers = response.info().headers

    # _, params = cgi.parse_header(
    #     [
    #         header for header in headers
    #         if 'Content-Disposition' in header
    #     ][0])

    bytes_count = float([
        header for header in headers
        if 'Content-Length' in header
    ][0].split(' ')[-1])

    # title = params['filename']

    body = []

    print '\r%d / %d [%d%%]' % (0, bytes_count, 0),
    for (progress, chunk) in read_in_chunks(response):
        print '\r%d / %d [%d%%]' % (progress, bytes_count, progress * 100 / bytes_count),
        body.append(chunk)

    # return title, ''.join(body)
    return 'Untitled', ''.join(body)


def download_from_url(url):
    page = urllib2.urlopen(url)

    bytes_count = float(page.headers['content-length'])
    body = []

    print '\r%d / %d [%d%%]' % (0, bytes_count, 0),
    for (progress, chunk) in read_in_chunks(page):
        print '\r%d / %d [%d%%]' % (progress, bytes_count, progress * 100 / bytes_count),
        body.append(chunk)

    return ''.join(body)
