import get_page_web

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

'''
unit 4: index

we modify the format to include click count for each url
[['keyword', [['url', count]]], [['keyword', [['url', count]]]]

define procedures that add to the index, and lookup in the index: '''

def add_to_index(index, keyword, url):
    for e in index:
        if e[0] == keyword:
            for u in e[1]:
                if u[0] == url:
                    return
            e[1].append([url, 0])
            return #interrupts the for loop
    index.append([keyword, [[url, 0]]])

def lookup(index, keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
    return []

def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    if urls:
        for u in urls:
            if u[0] == url:
                u[1] += 1

'''
index a whole page by splitting the content string into a list

first, introduce a procedure to split strings on punctuation: '''

def split_string(source, split_list):
    tokens_out = [source]
    tokens_sep = []
    for c in split_list:
        for token in tokens_out:
            tokens_new = token.split(c)
            for t in tokens_new:
                if t: #empty string is falsey
                    tokens_sep.append(t)
        tokens_out, tokens_sep = tokens_sep, []
    return tokens_out

def add_page_to_index(index, url, content):
    keywords = content.split()
    for k in keywords:
        add_to_index(index, k, url)

'''
define the crawler procedure

first, a utility procedure to combine lists without duplication: '''

def union(list1, list2):
    for e in list2:
        if e not in list1:
            list1.append(e)
    #return statement not needed, because input list is mutated

'''
this procedure will keep following the last link discovered on a given page
before returning to links discovered on earlier pages. hence it is known as a
depth-first search

change to breadth-first to limit depth of crawl. tutor's code: '''

def crawlWeb(seed, max_depth):
    toCrawl = [seed]
    crawled = []
    nextDepth = []
    depth = 0
    index = []
    while toCrawl and depth <= max_depth:
        page = toCrawl.pop()
        if page not in crawled:
            pageContent = get_page_web.get_page(page)
            add_page_to_index(index, page, pageContent)
            union(nextDepth, getAllURLs(pageContent))
            crawled.append(page)
        if not toCrawl:
            toCrawl, nextDepth = nextDepth, []
            depth += 1
    return index
