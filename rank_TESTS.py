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
'''
# list sort tests
print web_crawler.quicksort_descend([]) # []
print web_crawler.quicksort_descend([1]) # [1]
print web_crawler.quicksort_descend([2, 1]) # [2, 1]
print web_crawler.quicksort_descend([1, 2]) # [2, 1]
print web_crawler.quicksort_descend([1, 2, 3]) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2]) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2, 5, 4]) # [5, 4, 3, 2, 1]
'''
print web_crawler.quicksort_descend([], []) # []
print web_crawler.quicksort_descend([1], ['thing']) # [1]
print web_crawler.quicksort_descend([2, 1], ['thing2', 'thing1']) # [2, 1]
print web_crawler.quicksort_descend([1, 2], ['thing1', 'thing2']) # [2, 1]
print web_crawler.quicksort_descend([1, 2, 3], ['thing1', 'thing2', 'thing3']) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2], ['thing1', 'thing3', 'thing2']) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2, 5, 4], ['thing1', 'thing3', 'thing2', 'thing5', 'thing4']) # [5, 4, 3, 2, 1]
