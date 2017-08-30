from politics_lab import *

most_similar('Chafee', create_voting_dict())

voting_data = list(open("voting_record_dump109.txt"))

## Task 1
dictD = [x.split()[0] for x in voting_data if x.split()[1] == 'D' ]

dict = { x.split()[0]:x.split()[3:] for x in voting_data  }
dict = { x: [ int(y) for y in dict[x] ] for x in dict.keys() }

best = -10000
bestsen = ''
for sen in dict:
    avg = find_average_similarity(sen, dictD, dict) 
    if avg > best:
        best = avg
        bestsen = sen

print("avg democrat = ", best, bestsen)

print("avg dem rec=", find_average_record(dictD, dict))


