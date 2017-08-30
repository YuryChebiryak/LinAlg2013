from dictutil import *
# form the list of documents as strings

f = open('stories_small.txt')
strlist = list(f)

res = {}
for x in range(len(strlist)):
    for word in strlist[x].split():
        if word in res:
            res[word] = res[word] | {  x }
        else:
            res[word] = {x}

query = 'stretch time he'

inverseIndex = res

res2 = set()
first = True
for word in query.split():
    if word in inverseIndex:
        if first: 
            first = False; res2 = inverseIndex[word]
        else:
            res2 = res2 & inverseIndex[word]