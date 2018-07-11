import web_crawler
'''
seed = "https://udacity.github.io/cs101x/urank/"

index, graph = web_crawler.crawlWeb(seed)

ranks = web_crawler.compute_ranks(graph)

print ranks
'''
'''
#lucky search tests
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
'''
# quicksort tests
print web_crawler.quicksort_descend([], []) # []
print web_crawler.quicksort_descend([1], ['thing']) # [1]
print web_crawler.quicksort_descend([2, 1], ['thing2', 'thing1']) # [2, 1]
print web_crawler.quicksort_descend([1, 2], ['thing1', 'thing2']) # [2, 1]
print web_crawler.quicksort_descend([1, 2, 3], ['thing1', 'thing2', 'thing3']) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2], ['thing1', 'thing3', 'thing2']) # [3, 2, 1]
print web_crawler.quicksort_descend([1, 3, 2, 5, 4], ['thing1', 'thing3', 'thing2', 'thing5', 'thing4']) # [5, 4, 3, 2, 1]
'''
'''
# ordered search tests
print web_crawler.ordered_search(index, ranks, 'Hummus') # ...kathleen.html
print web_crawler.ordered_search(index, ranks, 'the') # ...nickel.html
print web_crawler.ordered_search(index, ranks, 'babaganoush') # none
'''
#reachable tests
g = {'a': ['a', 'b', 'c'], 'b':['a'], 'c':['d'], 'd':['a']}
print web_crawler.reachable_pages('a', g, 0) # ['a']
print web_crawler.reachable_pages('a', g, 1) # ['a']
print web_crawler.reachable_pages('a', g, 2) # ['a']

#reciprocal tests
print web_crawler.compute_ranks(g, 0) # the a->a link is reciprocal
#>>> {'a': 0.26676872354238684, 'c': 0.1216391112164609,
#     'b': 0.1216391112164609, 'd': 0.1476647842238683}

print web_crawler.compute_ranks(g, 1) # a->a, a->b, b->a links are reciprocal
#>>> {'a': 0.14761759762962962, 'c': 0.08936469270123457,
#     'b': 0.04999999999999999, 'd': 0.12202199703703702}

print web_crawler.compute_ranks(g, 2)
# a->a, a->b, b->a, a->c, c->d, d->a links are reciprocal
# (so all pages end up with the same rank)
#>>> {'a': 0.04999999999999999, 'c': 0.04999999999999999,
#     'b': 0.04999999999999999, 'd': 0.04999999999999999}
