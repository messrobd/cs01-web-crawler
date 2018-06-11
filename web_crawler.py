'''
procedural abstraction of code from unit 1. define a procedure (function) to
encapsulate the URL extraction: '''

def getURL(page): #could generalise to getTarget(string)
    start_link = page.find('<a href=')

    if start_link == -1: #handle the case where no links are found
        return None, 0

    openQuote = page.find('"', start_link)
    closeQuote = page.find('"', openQuote+1)

    url = page[openQuote + 1:closeQuote]

    return url, closeQuote 

'''
we know that we'll need to call the function multiple times to find multiple
links, so we return end_quote as well. the procedure doesn't change the value
of page so we don't want to do so just to return it.

define a procedure to get multiple URL's: '''

def getAllURLs(page):
    urlList = []
    while True:
        url, endPos = getURL(page)
        if url: #None is falsey
            urlList.append(url)
            page = page[endPos:]
        else:
            break
    return urlList
