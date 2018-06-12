import urllib

'''
encapsulate url request in a try-except so that consuming procedures don't need
to handle failed requests: '''

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except:
        return ''
