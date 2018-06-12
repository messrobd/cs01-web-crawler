import web_crawler

index = []

web_crawler.add_to_index(index,'udacity','http://udacity.com')
web_crawler.add_to_index(index,'computing','http://acm.org')
web_crawler.add_to_index(index,'udacity','http://npr.org')

print index
