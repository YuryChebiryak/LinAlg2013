from orthogonalization import *
from vecutil import *
from math import sqrt
from matutil import *

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    LL = orthogonalize(L)
    #for x in LL: print(x)
    #norms = [ sqrt(x*x) for x in LL ]
    #for x in norms: print(x)
    LL = [ (1/ sqrt(x*x)) * x for x in LL  ]
    #for x in LL: print(x)
    return LL

L = [ list2vec([4,3,1,2]), list2vec([8,9,-5,-5]), list2vec([10,1,-1,5]) ] 

def adjust(v, multipliers):
    return Vec(v.D, { d:v[d] * multipliers[d] for d in v.f.keys() })

def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    Qlist, Rlist = aug_orthogonalize(L)
    norms = [ sqrt(x*x) for x in Qlist ]
    #print("norms =" , norms)
    Qlist = [ (1/sqrt(x*x))*x for x in Qlist ]
    for x in range(0, len(Rlist)):
        Rlist[x] = adjust(Rlist[x], norms)#norms[x] * Rlist[x]
    return Qlist, Rlist

#L = [list2vec(v) for v in [[4,3,1,2],[8,9,-5,-5],[10,1,-1,5]]]
##print(coldict2mat(L))
#print("orthogonalize")
#Qlist, Rlist = aug_orthogonalize(L)
#print(coldict2mat(Qlist))
#print(coldict2mat(Rlist))
#print("orthonormalize")
#Qlist, Rlist = aug_orthonormalize(L)
#print(coldict2mat(Qlist))
#print(coldict2mat(Rlist))
#print(coldict2mat(Qlist) * coldict2mat(Rlist))

