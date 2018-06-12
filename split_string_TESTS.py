import web_crawler

out = web_crawler.split_string("This is a test-of the,string separation-code!"," ,!-")
print out
#>>> ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

out = web_crawler.split_string("After  the flood   ...  all the colors came out.", " .")
print out
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = web_crawler.split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print out
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']
