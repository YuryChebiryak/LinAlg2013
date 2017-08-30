from GF2 import one
from math import sqrt, pi
from matutil import coldict2mat
from solver import solve
from vec import Vec
from matutil import *
from vecutil import *

def solveprint(str, A, b):
    b = list2vec(b)
    s = solve(A, b )
    print(str, s)

def part1():
    S = listlist2mat([[2,0,4,0],[0,1,0,1],[0,0,-1,-1]])
    S = S.transpose()

    a = list2vec([2,1,4,1])
    s1 = solve(S,a)
    print("1.a=", s1)

    b = list2vec([1,1,1,0])
    s = solve(S, b)
    print("1.b=", s)

    c = list2vec([0,1,1,2])
    #solveprint("1c=", S, c)

    S = listlist2mat([[0,0,1],[2,0,1],[4,1,2]])
    S = S.transpose()
    a = list2vec([2,1,4])
    b = list2vec([1,1,1])
    c = list2vec([5,4,3])
    d = list2vec([0,1,1])
    #solveprint("2a", S, a)
    #solveprint("2b", S, b)
    #solveprint("2c", S, c)
    #solveprint("2d", S, d)

    S = listlist2mat([[0,one,0,one],[0,0,one,0],[one,0,0,one],[one,one,one,one]])
    S = S.transpose()
    solveprint("3a", S, [one,one,0,0])
    solveprint("3b", S , [one,0,one,0])
    solveprint("3c", S, [one,0,0,0])

    G = listlist2mat([[one,one,0,0,0,0,0,0],\
                      [0,one,one,0,0,0,0,0],\
                      [one,0,0,one,0,0,0,0],\
                      [0,one,0,0,one,0,0,0],\
                      [0,0,one,0,one,0,0,0],\
                      [0,0,0,one,one,0,0,0],\
                      [0,0,0,0,0,one,0,one],\
                      [0,0,0,0,0,0,one,one]])
    G = G.transpose()
    solveprint("4a", G, [0,0,one,one,0,0,0,0])
    solveprint("4b", G, [0,0,0,0,0,one,one,0])
    solveprint("4c", G, [one,0,0,0,one,0,0,0])
    solveprint("4d", G, [0,one,0,one,0,0,0,0])

def part2():
    S = listlist2mat([[1,2,0],[2,4,1]])
    S = S.transpose()
    solveprint("5a", S, [0,0,-1])
    S = listlist2mat([[2,4,0],[8,16,4]])
    S = S.transpose()
    solveprint("5b", S , [0,0,7])
    S = listlist2mat([[0,0,5],[1,34,2],[-3,-6,0],[1,2,0.5]])#[-3,-6,0]])
    S = S.transpose()
    solveprint("5c", S, [123,456,789])
    S = listlist2mat([[1,2,3],[4,5,6]])
    S = S.transpose()
    solveprint("6a", S, [1,1,1])
    S = listlist2mat([[0,-1,0,-1],[pi,pi,pi,pi]])
    S = S.transpose()
    solveprint("6b", S, [-sqrt(2), sqrt(2), -sqrt(2), sqrt(2)])
    S = listlist2mat([[1,-1,0,0,0],[0,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1]])
    S= S.transpose()
    solveprint("6c", S, [-1,0,0,0,1])
    S = listlist2mat([[3,9,6,5,5],[4,10,6,6,8]])
    S = S.transpose()
    solveprint("7a", S, [1,1,0,1,3])
    S = listlist2mat([[one,one,one,one],[one,0,one,0],[0,one,one,0]])
    S = S.transpose()
    solveprint("9a", S, [0,one,0,one])
    S = listlist2mat([[0,0,0,one],[0,0,one,0],[one,one,0,one]])
    S = S.transpose()
    solveprint("9b", S, [one,one,one,one])
    S = listlist2mat([[one,one,0,one,one],[0,0,one,0,0],[0,0,one,one,one],[one,0,one,one,one]])
    S = S.transpose()
    solveprint("9c", S, [one,one,one,one,one])

def test():
    part2()



if __name__ == '__main__':
    test()
