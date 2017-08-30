from mat import Mat
from vec import Vec
from matutil import *
from GF2 import one
from vecutil import *
from solver import *

M1 = Mat(({1,2}, ({1,2})), { (1,1):1, (1,2):1, (2,1):1, (2,2):-1 })
V1 = Vec({1,2}, {1:0.5, 2:0.5})
print("P1.1 = ", M1 * V1)

M1 = Mat(({1,2}, ({1,2})), { (1,1):0, (1,2):0, (2,1):0, (2,2):1 })
V1 = Vec({1,2}, {1:1.2, 2:4.44})
print("P1.2 = ", M1 * V1)

M1 = Mat(({1,2,3}, ({1,2,3})), { (1,1):1, (1,2):2, (1,3):3, (2,1):2, (2,2):3, (2,3):4, (3,1):3, (3,2):4, (3,3):5 })
V1 = Vec({1,2,3}, {1:1, 2:2, 3:3})
print("P1.3 = ", M1 * V1)

M0 = Mat(({0,1,2}, ({0,1,2})), { (0,0):1, (0,1):2, (0,2):3, (1,0):2, (1,1):3, (1,2):4, (2,0):3, (2,1):4, (2,2):5 })

A = listlist2mat( [ [2,3],[4,2] ])
B = listlist2mat( [[1,2],[2,3]])
print("6.1=",A*B)

A = listlist2mat( [[2,4,1],[3,0,-1]])
B = listlist2mat( [[1,2,0],[5,1,1],[2,3,0]])
print("6.2=", A*B)

A = listlist2mat( [[ 2,2,1]])
B = listlist2mat( [[3,1],[-2,6],[1,-1]])
print("6.3=", A*B)

A = listlist2mat( [[1,2,3]])
B = listlist2mat( [[1],[2],[3]])
print("6.4=", A*B)

print("6.5=", B*A)

A = listlist2mat( [[4,1,-3],[2,2,-2]])
B = listlist2mat( [[-1,1],[1,0]])

print("6.6=", A.transpose()*B)

A = listlist2mat( [[2,0,1,5],[1,-4,6,2],[3,0,-4,2],[3,4,0,-2]])
B = listlist2mat( [[0,1,0,0],[0,0,1,0],[0,0,0,1],[1,0,0,0]])
print("7.1=", A*B)
print(B*A)

B = listlist2mat( [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]])
print("7.2=", A*B)
print(B*A)

B = listlist2mat( [[0,0,0,1],[0,1,0,0],[1,0,0,0],[0,0,1,0]])
print("7.3=", A*B)
print(B*A)

print("10.a=", listlist2mat( [[2,3,1],[1,3,4]]) * listlist2mat( [[2],[2],[3]]))
print("10.b =", listlist2mat( [[2,4,1,]]) * listlist2mat( [[1,2,0],[5,1,1],[2,3,0]]))

print("10.c=", listlist2mat( [[2,1]]) * listlist2mat( [[3,1,5,2],[-2,6,1,-1]]))
print("10d.= ", listlist2mat( [[1,2,3,4],[1,1,3,1]]) * listlist2mat( [[1],[2],[3],[4]]))
A = listlist2mat( [[4],[1],[-3]])
print("10e=", A.transpose()* listlist2mat( [[-1,1,1],[1,0,2],[0,1,-1]]))

M = listlist2mat([[-1,1,2],[1,2,3],[2,2,1]])
v = list2vec([1,2,0])

A = listlist2mat([[3,4],[2,1]])
b= list2vec([1,0])
s1 = solve(A,b)
print("18.1=", s1)

A = listlist2mat([[3,4],[2,1]])
b= list2vec([0,1])
s2 = solve(A,b)
print("18.2=", s2)

A = listlist2mat([[5,1],[9,2]]) 
B = listlist2mat([[2,-1],[-9,5]])
print("19.1 A*B, B*A", A*B, B*A)

A = listlist2mat([[2,0],[0,1]])
B= listlist2mat([[0.5,0],[0,1]])
print("19.2 A*B, B*A", A*B, B*A)


A = listlist2mat([[3,1],[0,2]])
B= listlist2mat([[1,1/6],[-2,1/2]])
print("19.3 A*B, B*A", A*B, B*A)

A = listlist2mat([[one,0,one],[0,one,0]])
B= listlist2mat([[0,one],[0,one],[0,one]])
print("19.4 A*B, B*A", A*B, B*A)

A = listlist2mat([[3,4],[2,1]])
B = Mat(({0, 1}, {0, 1}), {(0,0):-0.2, (0,1):0.8, (1,0):0.4, (1,1):-0.6})

M = listlist2mat([[1,2,3],[10,20,30]])
v = list2vec([7,0,4])