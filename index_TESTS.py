import web_crawler

index = []

web_crawler.add_to_index(index,'udacity','http://udacity.com')
web_crawler.add_to_index(index,'computing','http://acm.org')
web_crawler.add_to_index(index,'udacity','http://npr.org')

print index
print web_crawler.lookup(index,'udacity')

index = []

web_crawler.add_page_to_index(index,'fake.text',"This is a test")
web_crawler.add_page_to_index(index,'so_fake.text',"This is still a test")
print index

seed = 'http://www.udacity.com/cs101x/index.html'
#print web_crawler.crawlWeb(seed, 3)

def test_add():
    index = []
    content = [
    ["http://some.page/stuff.html","hello hello"],
    ["http://other.page/morestuff.html", 'Good <a href="http://this.page/otherstuff.html">night</a>, sleep tight, go to bed and dream of Python'],
    ["http://this.page/otherstuff.html","Wake up, wake up, the morning is here! It's time to go to work!"]
    ]
    for page in content:
        web_crawler.add_page_to_index(index, page[0], page[1])
    return index

print test_add()
