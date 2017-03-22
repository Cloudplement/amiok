import urllib.request

def get_status(url):
    """ This function gets the status code of a website.
        A response of 200 if the website is okay
    """
    try:
        conn = urllib.request.urlopen(url)
        if conn.getcode() == 200:
            return "OK"
    except urllib.error.URLError:
        return "Not OK"

print(get_status("http://google.com"))
print(get_status("http://not-google-domain.com"))
