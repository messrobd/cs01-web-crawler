import web_crawler

seed = "https://udacity.github.io/cs101x/urank/"

index, graph = web_crawler.crawlWeb(seed)

ranks = web_crawler.compute_ranks(graph)

print ranks

print web_crawler.lucky_search(index, ranks, 'Hummus') # ...kathleen.html
print web_crawler.lucky_search(index, ranks, 'the') # ...nickel.html
print web_crawler.lucky_search(index, ranks, 'babaganoush') # none 
