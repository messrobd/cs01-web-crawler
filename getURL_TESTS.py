import web_crawler

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

url, endPos = web_crawler.getURL(page)

print url #http://udacity.com

print web_crawler.getAllURLs(page) #['http://udacity.com']

'''
tests for obsolete depth-first method
seed = "http://xkcd.com/353"

print len(web_crawler.crawlWeb(seed, 100)), web_crawler.crawlWeb(seed, 100) #31
print len(web_crawler.crawlWeb(seed, 10)), web_crawler.crawlWeb(seed, 10) #10 '''

seed = "http://xkcd.com/353"

print web_crawler.crawlWeb(seed,3) 
