# version code 988
# Please fill out this stencil and submit using the provided submission script.
from math import sqrt
from matutil import *
from GF2 import one
from vecutil import zero_vec
import echelon
from vecutil import *
## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[  1,2,0,2,0   ],
                  [  0,1,0,3,4  ],
                  [  0,0,2,3,4   ],
                  [  0,0,0,2,0   ],
                  [  0,0,0,0,4  ]]

echelon_form_2 = [[   0,4,3,4,4  ],
                  [   0,0,4,2,0   ],
                  [   0,0,0,0,1   ],
                  [   0,0,0,0,0   ]]

echelon_form_3 = [[   1,0,0,1  ],
                  [   0,0,0,1   ],
                  [   0,0,0,0   ]]

echelon_form_4 = [[   1,0,0,0  ],
                  [   0,1,0,0   ],
                  [   0,0,0,0   ],
                  [   0,0,0,0   ]]



## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon([[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    first = -1
    for x in A:
        if not len(x): return True
        indices = [i for i,e in enumerate(x) if e!=0 ]
        if not len(indices):
            current = len(x)
        else:
            current = min(indices)
        if current <= first and not ( ( first == len(x)) and (current == len(x))):
            return False
        first = current
    return True



## Problem 3
# Give each answer as a list

echelon_form_vec_a = [1,0,3,0]
echelon_form_vec_b = [(1-9+2) /2,0,-2,3]
echelon_form_vec_c = [(2-4-8)/2,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]



## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]
    >>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    D = rowlist[0].D
    x = zero_vec(D)
    for j in reversed(range(len(D))):
        if j >= len(rowlist): continue
        indices = [ i for i in range(len(label_list)) if rowlist[j][label_list[i]] ]
        #indices = [i for i,e in enumerate(j) if e!=0 ]
        if not len(indices):
            continue
        ind = indices[0]
        c = label_list[ind]
        row = rowlist[j]
        x[c] = b[j] + x*row  # + row[c]
    #print ("x=", x)
    return x

D = {'A','B','C','D','E'}
U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
b_list = [one,0,one]
cols = ['A', 'B', 'C', 'D', 'E']
echelon_solve(U_rows, cols, b_list)

#cols = ['A','B','C','D','E']
#D = set(cols)
#U_rows = [Vec(D,{'E': one, 'D': one, 'A': 0, 'C': 0, 'B': one}), \
#    Vec(D,{'E': 0, 'D': one, 'A': 0, 'C': 0, 'B': 0}), \
#    Vec(D,{'E': 0, 'D': 0, 'A': one, 'C': one, 'B': 0}),\
#    Vec(D,{'E': 0, 'D': 0, 'A': 0, 'C': 0, 'B': 0})]
#b_list = [0, 0, one, 0]
#u = echelon_solve(U_rows, cols, b_list)
#print(u)

#U_rows = [Vec(D, {'A':one, 'C':one}), Vec(D, {'C':one, 'E':one}), Vec(D,{'D' :one})]
#b_list = [one, one, one]
#u = echelon_solve(U_rows, cols, b_list)
#print( u)

## Problem 6
def solve(A,b):
    M = echelon.transformation(A)
    U = M * A
    col_label_list = sorted(A.D[1])
    U_rows_dict = mat2rowdict(U)
    rowlist = [ U_rows_dict[i] for i in U_rows_dict ]
    print("A=", A)
    print("M = ", M)
    print("M*A", M*A)
    print("rowlist = ", rowlist)
    print("labels=", col_label_list)
    print("b=", M*b)
    return echelon_solve(rowlist, col_label_list, M*b)

A = Mat( ({'a','b','c','d'}, {'A','B','C','D'}), { ('a','A'):one, ('a','B'):one, ('a,','C'):0, ('a','D'):one, \
                                                  ('b','A'): one, ('b','B'): 0, ('b','C'): 0, ('b','D'): one,\
                                                  ('c','A'):one , ('c','B'): one, ('c','C'): one, ('c','D'): one,\
                                                  ('d','A'): 0, ('d','B'): 0, ('d','C'): one,('d','D'):one })

g = Vec({'a','b','c','d'}, {'a':one,'c':one})
#solve(A,g)

M = Mat( ({0,1,2,3}, {'a','b','c','d'}), { (0,'a'):one, (1,'a'):one, (1,'b'):one, (2,'a'):one, (2,'c'):one, (3,'a'):one, (3,'c'):one, (3,'d'):one } )

#print("MA=", M * A)
#print("b = ", M*g)
#rows = [ mat2rowdict(M * A)[i] for i in mat2rowdict(M * A) ]
#print("rows = ", rows)

rowlist = [Vec({'D', 'C', 'B', 'A'},{'D': one, 'C': 0, 'B': one, 'A': one}), Vec({'D', 'C', 'B', 'A'},{'D': 0, 'C': 0, 'B': one, 'A': 0}), Vec({'D', 'C', 'B', 'A'},{'D': 0, 'C': one, 'B': 0, 'A': 0}), Vec({'D', 'C', 'B', 'A'},{'D': one, 'C': 0, 'B': 0, 'A': 0})]    # Provide as a list of Vec instances
label_list = ['A', 'B', 'C', 'D'] # Provide as a list
b = [ one,one,0,0 ]          # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
#def project_along(b, a): return ((b*a)/(a*a) if a*a != 0 else 0)*a
def project_along(b, a): 
    sigma = (b*a)/(a*a) if a*a > 1e-20 else 0
    return sigma * a

def project_orthogonal(b, a): return b - project_along(b, a)
a = list2vec([1,2])
b= list2vec([2,3])
print("9.1=", project_along(b,a))
a = list2vec([0,1,0])
b=list2vec([1.414, 1, 1.732])
print("9.2=", project_along(b,a))
a = list2vec([-3,-2,-1,4])
b=list2vec([7,2,5,0])
print("9.3=", project_along(b,a))

closest_vector_1 = [1.6,3.2]
closest_vector_2 = [0,1,0]
closest_vector_3 = [3,2,1,-4]



## Problem 10
# Write each vector as a list
a=list2vec([3,0])
b=list2vec([2,1])
print("10.1=", project_along(b,a))
print(project_orthogonal(b,a))
a = list2vec([1,2,-1])
b=list2vec([1,1,4])
print("10.2=", project_along(b,a))
print(project_orthogonal(b,a))
print(project_orthogonal(b,a)[0], project_orthogonal(b,a)[1], project_orthogonal(b,a)[2])


a = list2vec([3,3,12])
b=list2vec([1,1,4])
print("10.3=", project_along(b,a))
print(project_orthogonal(b,a))

project_onto_1 = [2,0]
projection_orthogonal_1 = [0,1]

project_onto_2 = [-1/6, -1/3, 1/6]
projection_orthogonal_2 = [7/6,4/3,23/6]

project_onto_3 = [1,1,4]
projection_orthogonal_3 = [0,0,0]



## Problem 11
def norm(v): return sqrt( v * v)
v1 = list2vec([2,2,1])
v2 = list2vec([sqrt(2), sqrt(3), sqrt(5), sqrt(6)])

print("11.1=", norm(v1))
print("11.2=", norm(v2))

norm1 = 3
norm2 = 4
norm3 = 1

