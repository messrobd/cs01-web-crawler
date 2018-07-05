import web_crawler

seed = "https://udacity.github.io/cs101x/urank/"

index, graph = web_crawler.crawlWeb(seed)

ranks = web_crawler.compute_ranks(graph)

'''
print ranks

print web_crawler.lucky_search(index, ranks, 'Hummus') # ...kathleen.html
print web_crawler.lucky_search(index, ranks, 'the') # ...nickel.html
print web_crawler.lucky_search(index, ranks, 'babaganoush') # none
'''
print web_crawler.quicksort_descend([]) # []
print web_crawler.quicksort_descend([1]) # [1]
print web_crawler.quicksort_descend([2, 1]) # [2, 1]
print web_crawler.quicksort_descend([1, 2]) # [2, 1]
print web_crawler.quicksort_descend([1, 2, 3]) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2]) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2, 5, 4]) # [5, 4, 3, 2, 1]
