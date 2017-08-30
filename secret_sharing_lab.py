# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
import independence
import itertools
from vec import *


## Problem 1
def randGF2(): return random.randint(0,1)*one
def randvec(length):
    return list2vec( [ random.randint(0,1)*one for _ in range(length) ])

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    u = randvec(len(a0.D))
    while not ((a0 * u == s) and (b0 * u == t)):
        u = randvec(len(a0.D))
        #print(u)
    #print("return = ", u)
    return u

print(randvec(6))
print(randvec(6))
print("choose1", choose_secret_vector(0,one))
print(choose_secret_vector(one,one))
print(choose_secret_vector(one,0))
print(choose_secret_vector(0,0))



## Problem 2
# Give each vector as a Vec instance
def pairwise_indep(pairs, k):
    for comb in itertools.combinations(pairs, k):
        lst = []
        for x in comb:
            lst = lst + x
        if not independence.is_independent(lst):
            return False
    return True

def find_vecs():
    a1 = randvec(6)
    b1 = randvec(6)
    a2 = randvec(6)
    b2 = randvec(6)
    a3 = randvec(6)
    b3 = randvec(6)
    a4 = randvec(6)
    b4 = randvec(6)
    pairs = [ [a0,b0], [a1,b1], [a2,b2], [a3, b3], [a4,b4] ]
    while not pairwise_indep(pairs, 3):
        a1 = randvec(6)
        b1 = randvec(6)
        a2 = randvec(6)
        b2 = randvec(6)
        a3 = randvec(6)
        b3 = randvec(6)
        a4 = randvec(6)
        b4 = randvec(6) 
        pairs = [ [a0,b0], [a1,b1], [a2,b2], [a3, b3], [a4,b4] ]   
    print(pairs)
    print(a0, b0, a1, b1,a2,b2,a3,b3,a4,b4)
    
    #while not ( independence.is_independent([a0, b0, a1, b1, a2, b2]) and \
    #           independence.is_independent([a0,b0,a1,b1,a3,b3]) and \
    #           independence.is_independent([a0,b0,a1,b1,a4,b4]) and \
    #           independence.is_independent([]) and \ 
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \
    #           independence.is_independent([]) and \)

 
secret_a0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: 0, 5: one})
secret_b0 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: 0, 4: 0, 5: one})
secret_a1 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: one, 3: 0, 4: one, 5: 0})
secret_b1 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: one, 4: 0, 5: one})
secret_a2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 0, 3: one, 4: one, 5: 0})
secret_b2 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: one, 3: one, 4: 0, 5: one})
secret_a3 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: 0, 2: one, 3: one, 4: one, 5: one})
secret_b3 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: one, 5: 0})
secret_a4 = Vec({0, 1, 2, 3, 4, 5},{0: one, 1: one, 2: 0, 3: one, 4: one, 5: 0})
secret_b4 = Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: one, 2: 0, 3: 0, 4: one, 5: one})

