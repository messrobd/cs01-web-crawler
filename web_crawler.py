from get_page_web import get_page

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
            pageContent = get_page(page)
            add_page_to_index(index, page, pageContent)
            outlinks = getAllURLs(pageContent)
            graph[page] = outlinks
            union(toCrawl, outlinks)
            crawled.append(page)
    return index, graph

'''
compute ranks

rank(0, url) ==> 1 / N
rank(t, url) ==> d * sum( links[url]( rank(t - 1, p) / urls[p] ) ) + (1-d) / N

outline function from tutor's code

for loop preferred to recursion. algorithm is equivalent because
* in iteration t, rank of all a page's inlinks are added to its own
* still in iteration t, the rank of every page's inlinks is recomputed the same
way
* in iteration t + 1, the process is repeated, but now the ranks of all a
page's inlinks have been recomputed '''

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

'''
feeling lucky (lesson 23: prob set, #5)

given an index, a ranks dic and a keyword, return the highest ranked result '''

def lucky_search(index, ranks, keyword):
    if keyword in index:
        candidates = index[keyword]
        result = candidates[0]
        for c in candidates:
            result = c if ranks[c] > ranks[result] else result # py ternary statement
        return result
    else:
        return None

'''
ordered search (lesson 24: prob set, #3)

given a keyword, return a set of results sorted on rank (descending)

tip: use quicksort (hoare '59)
  1. lists with 0 or 1 element are already sorted
  2. pick a pivot
  3. create 2 lists, one greater than the pivot, and one less than
  4. concatenate the 3 resulting lists to give the sorted result

sorted([]) ==> true
sorted([n]) ==> true
sorted([n0, n1]) ==> n0 > n
sorted([n0 ... nn]) ==> sorted(n0, sorted([n1 ... nn]))
sorted([n]) ==> sorted([<n]) + n + sorted([>n])'''

def quicksort_descend_L(inlist):
    if len(inlist) == 0 or len(inlist) == 1:
        return inlist
    pivot = inlist[0]
    unsorted = inlist[1:]
    lt = []
    gt = []
    for n in unsorted:
        if n <= pivot:
            lt = quicksort_descend(lt + [n])
        elif n > pivot:
            gt = quicksort_descend(gt + [n])
    return gt + [pivot] + lt

def quicksort_descend(vlist, keylist):
    if len(vlist) == 0 or len(vlist) == 1:
        return vlist, keylist
    pivot, pivot_key = vlist[0], keylist[0]
    unsorted, unsorted_keys = vlist[1:], keylist[1:]
    lt, lt_keys = [], []
    gt, gt_keys = [], []
    for i, n in enumerate(unsorted):
        if n <= pivot:
            lt, lt_keys = quicksort_descend(lt + [n], lt_keys + [unsorted_keys[i]])
        elif n > pivot:
            gt, gt_keys = quicksort_descend(gt + [n], gt_keys + [unsorted_keys[i]])
    sorted_values = gt + [pivot] + lt
    sorted_keys = gt_keys + [pivot_key] + lt_keys
    return sorted_values, sorted_keys

def ordered_search(index, ranks, keyword):
    if keyword in index:
        candidates = index[keyword]
        candidates_ranked = {}
        for c in candidates:
            candidates_ranked[c] = ranks[c]
        unsorted_ranks, unsorted_urls = candidates_ranked.values(), candidates_ranked.keys()
        return quicksort_descend(unsorted_ranks, unsorted_urls)[1]
    else:
        return None
