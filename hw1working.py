from GF2 import one
from itertools import *
from vec import Vec
from math import sqrt

def subtrn(v,u): return [ (v[x] - u[x]) for x in range(0, len(u))]

def addn(v,w): return [ (v[x] + w[x]) for x in range( len(v))]

def dotpn(v,w): return sum ([ (v[x] * w[x]) for x in range(len(v)) ])

def addlist(l, D):
    sum = [0] * D
    for vec in l:
        sum = addn(sum, vec)
    return sum

def scalar(v, alpha): return [alpha * x for x in v]

def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )

def subsetsums(vectors, u):
    D = len(u)
    sums = []
    comb = combinations(vectors)
    for x in comb:
        if len(x) == 0:
            pass
        sum = u
        sum = addn(sum, addlist([ list(vectors[y]) for y in x  ], D))
        #sum = u.copy()
        #for y in x:
        #    sum = addn(sum, vectors[y])
        if sum == [0,0,0,0,0,0,0]:
            sums.append(list(x))
    return sums

def triangular(rowlist, b):
    x = [0] * len(rowlist[0])
    for i in reversed(range(len(rowlist))):
        x[i] = (b[i] - dotpn(rowlist[i],  x)) / rowlist[i][i]
    return x

rowlist7 = [ [one, one, 0, 0], [one, 0, one, 0], [one, one, one, one] ]
b7 = [one, one, one]
#print ("res7 ", triangular(rowlist7, b7))
print("res7" , [ [a,b,c,d] for a in {0, one} for b in {0, one} for c in {0, one} for d in {0, one} if dotpn([a,b,c,d], rowlist7[0]) == b7[0] and dotpn([a,b,c,d], rowlist7[1]) == b7[1] and dotpn([a,b,c,d], rowlist7[2]) == b7[2] ])

prob4 = { 'a':[one, one, 0,0,0,0,0], 'b':[0,one,one,0,0,0,0], 'c':[0,0,one,one,0,0,0],
         'd': [0,0,0,one,one,0,0], 'e':[0,0,0,0,one,one,0], 'f': [0,0,0,0,0,one,one] }

prob5 = { 'a':[one,one,one,0,0,0,0],
         'b':[0,one,one,one,0,0,0],
         'c':[0,0,one,one,one,0,0],
         'd':[0,0,0,one,one,one,0],
         'e':[0,0,0,0,one,one,one],
         'f':[0,0,0,0,0,one,one] }

u = [0,0,one,0,0,one,0]

print(" res= ", subsetsums(prob4.copy(), u))

u2 = [0,one,0,0,0,one,0]
print("res2=", subsetsums(prob4.copy(), u2))

u3 = [0,0,one,0,0,one,0]

u4 = [0,one,0,0,0,one,0]
print("res5.1=", subsetsums(prob5.copy(),u3))
print("res5.2=", subsetsums(prob5.copy(), u4))

u = Vec({'0','1'}, {'0':1, '1':0})
v = Vec({'0','1'}, {'0':5, '1':4321})
print ("res 6.a=" , u*v)

print("res 6.b =", Vec(range(2), {0:0, 1:1}) * Vec(range(2), {0:12345, 1:6}))

print("res 6.c =", Vec(range(2), {0:-1, 1:3}) * Vec(range(2), {0:5, 1:7}))

print("res 6.d =", Vec(range(2), {0: (-sqrt(2)/2), 1:sqrt(2)/2}) * Vec(range(2), {0:  sqrt(2)/2, 1: -sqrt(2)/2 }))

p1_u = [ 0, 4]
p1_v = [-1, 3]
p1_v_plus_u = [ -1, 7]
p1_v_minus_u = [-1,-1]

u = Vec(range(2), {0:0, 1:4})
v = Vec(range(2), {0:-1, 1:3})

p1_three_v_minus_two_u = (3 * v) - (2 * u)
print("1.3= ", p1_three_v_minus_two_u)