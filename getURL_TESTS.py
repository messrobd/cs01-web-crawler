import web_crawler

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

url, endPos = web_crawler.getURL(page)

print url #http://udacity.com

print web_crawler.getAllURLs(page) #['http://udacity.com']
