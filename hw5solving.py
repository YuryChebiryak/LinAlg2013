
from vecutil import list2vec
from solver import solve
from matutil import listlist2mat, coldict2mat
from mat import Mat
from GF2 import one
from vec import Vec
from hw4 import *
from matutil import *
from vecutil import *
from hw5 import *

def tasks1_2():
    w0 = list2vec([1,0,0])
    w1 = list2vec([0,1,0])
    w2 = list2vec([0,0,1])

    v0 = list2vec([1,2,3])
    v1 = list2vec([1,3,3])
    v2 = list2vec([0,3,3])

    exchange_S0 = [w0, w1, w2]

    w = exchange(exchange_S0, [], v0)
    exchange_S1 = [ x for x in exchange_S0 if x != w ] + [ v0 ]
    print (w)

    w = exchange(exchange_S1, [v0], v1)
    exchange_S2 = [ x for x in exchange_S1 if x != w] + [ v1 ]

    print(w)

    w = exchange(exchange_S2, [v0, v1], v2)
    print(w)

    w0 = list2vec([0,one,0])
    w1 = list2vec([0,0,one])
    w2 = list2vec([one,one,one])

    v0 = list2vec([one,0,one])
    v1 = list2vec([one,0,0])
    v2 = list2vec([one,one,0])

    exchange_2_S0 = [w0, w1, w2]

    A = []
    Z = [v0,v1,v2]
    while len(Z) > 0 and exchange(exchange_2_S0, A, Z[0]):
        print(exchange(exchange_2_S0, A, Z[0]))
        exchange_2_S0.remove(exchange(exchange_2_S0, A, Z[0]))
        exchange_2_S0.append(Z[0])
        A.append(Z[0])
        del Z[0]

def task_4():
    rows = [ list2vec([1,2,0]), list2vec([0,2,1]) ]
    superset_basis([], rows)
    cols = [ list2vec([1,0]), list2vec([2,2]), list2vec([0,1]) ]
    superset_basis([], cols)
    rows = [ list2vec([1,4,0,0]), list2vec([0,2,2,0]), list2vec([0,0,1,1]) ]
    cols = [ list2vec([1,0,0]), list2vec([4,2,0]), list2vec([0,2,1]), list2vec([0,0,1]) ]
    print("4.2 = ", superset_basis([], rows))
    print(superset_basis([], cols))
    rows = [ list2vec([1]), list2vec([2]), list2vec([3]) ]
    cols = [ list2vec([1,2,3])]
    print("4.3 = ", superset_basis([], rows))
    print(superset_basis([], cols))
    rows = [ list2vec([1,0]), list2vec([2,1]), list2vec([3,4]) ]
    cols = [list2vec([1,2,3]), list2vec([0,1,4]) ]
    print("4.4 = ", superset_basis([], rows))
    print(superset_basis([], cols))

def task_5():
    L = [Vec({0, 1, 2},{0: 1, 1: 0, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 1})]
    assert( my_is_independent(L) == False)    
    assert( my_is_independent(L[:2]))
    assert( my_is_independent(L[:3]))
    assert( my_is_independent(L[1:4]))
    assert(not my_is_independent(L[0:4]))
    assert(not my_is_independent(L[2:]))
    assert(not my_is_independent(L[2:5]))
    print("PASS")

def task_6():
    a0 = Vec({'a','b','c','d'}, {'a':1})
    a1 = Vec({'a','b','c','d'}, {'b':1})
    a2 = Vec({'a','b','c','d'}, {'c':1})
    a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
    assert( subset_basis([a0,a1,a2,a3]) == [Vec({'c', 'b', 'a', 'd'},{'a': 1}), Vec({'c', 'b', 'a', 'd'},{'b': 1}), Vec({'c', 'b', 'a', 'd'},{'c': 1})])
    print("PASS")

def task_7():
    assert(my_rank([list2vec(v) for v in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]]) == 2)
    print("PASS 7")

def task_8():
    U = listlist2mat([[one, 0], [0,0], [one, one], [0,0]])
    V = listlist2mat([[0,0],[one,0],[0,0],[one,one]])
    zero = list2vec([0,0,0,0])
    u = solve(U, zero)
    print(u)
    v = solve(V, zero)
    print(v)
    print("TRUE")
    U = listlist2mat([ [1,1], [2,2], [3,0]])
    V = listlist2mat( [[2,1,3], [2,1,3]])
    V = V.transpose()
    zero = list2vec([0,0,0])
    u = solve(U,zero)
    print(u)
    v = solve(V, zero)
    print(v)
    print("TRUE")
    U = listlist2mat([ [2,0,8,0], [1,1,4,0]])
    U = U.transpose()
    V = listlist2mat([ [2,1,1,1], [0,1,1,1]] )
    V = V.transpose()
    u = solve(U, zero)
    v = solve(V, zero)
    print(u , v)
    print("True")

def task_9():
    U_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
    V_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
    w = Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
    veclist = [ u + v for u in U_basis for v in V_basis]
    for x in  veclist:
        print (x)
    print(vec2rep(veclist, w))

    #u = solve(U,Wu)    
    #v = solve(V,Wv)    
#    return (u,v)
    assert(direct_sum_decompose(U_basis, V_basis, w)) == (Vec({0, 1, 2, 3, 4, 5},{0: 2.0, 1: 4.999999999999972, 2: 0.0, 3: 0.0, 4: 1.0, 5: 0.0}), Vec({0, 1, 2, 3, 4, 5},{0: 0.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 0.0}))

def task_10():
    M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
    assert( is_invertible(M))
    print("Pass 10")

def task_11():
    M = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (1, 2): 0, (0, 0): 0, (2, 0): 0, (1, 0): one, (2, 2): one, (0, 2): 0, (2, 1): 0, (1, 1): 0})
    assert (find_matrix_inverse(M) == Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): one, (2, 0): 0, (0, 0): 0, (2, 2): one, (1, 0): one, (1, 2): 0, (1, 1): 0, (2, 1): 0, (0, 2): 0}) )

def task_12():
    A = listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
    assert( find_triangular_matrix_inverse(A) == Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): -0.5, (1, 2): -0.3, (3, 2): 0.0, (0, 0): 1.0, (3, 3): 1.0, (3, 0): 0.0, (3, 1): 0.0, (2, 1): 0.0, (0, 2): -0.05000000000000002, (2, 0): 0.0, (1, 3): -0.87, (2, 3): -0.1, (2, 2): 1.0, (1, 0): 0.0, (0, 3): -3.545, (1, 1): 1.0}) )

if __name__ == '__main__':
    task_12()