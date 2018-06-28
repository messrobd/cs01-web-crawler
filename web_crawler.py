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

we modify the representation of the index to a dictionary to improve
scalability. properties:
'keyword1': ['url'],
'keyword2': ['url']

define procedures that add to the index, and lookup in the index: '''

def add_to_index(index, keyword, url):
    if keyword in index:
        urls = index[keyword]
        if url in urls:
            return
        else:
            urls.append(url)
    else:
        index[keyword] = [url]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None

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

change to dictionary representation of index, to improve scalability: '''

def crawlWeb(seed):
    toCrawl = [seed]
    crawled = []
    graph = {}
    index = {}
    while toCrawl:
        page = toCrawl.pop()
        if page not in crawled:
            pageContent = get_page_web.get_page(page)
            add_page_to_index(index, page, pageContent)
            outlinks = getAllURLs(pageContent)
            graph[page] = outlinks
            union(toCrawl, outlinks)
            crawled.append(page)
    return index, graph

'''
compue ranks '''

def compute_ranks(graph):
    d = 0.8 # damping factor
    numloops = 10 # relaxation iterations

    ranks = {}
    npages = len(graph)
    for page in graph:
        ranks[page] = 1.0 / npages

    for i in range(0, numloops):
        newranks = {}
        for page in graph:
            newrank = (1 - d) / npages
            for source in graph:
                if source != page:
                    outlinks = graph[source]
                    if page in outlinks:
                        newrank += (d * ranks[source]) / len(outlinks)
            newranks[page] = newrank
        ranks = newranks 

    return ranks
