from mat import *
from vec import *
from cancer_data import *
from vecutil import *
from matutil import *
import math
## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D, { x:+1  if u[x] >= 0 else -1 for x in u.D })
    

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''
    d = signum(A * w ) * signum(b)
    #print(d)
    return 1 - (d + len(A.D[0])) / len(A.D[0]) / 2

## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    return (A * w - b ) * (A * w - b)
    

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    vec = (A * w - b) * A
    summ = 2 * vec
    return summ

A1 = listlist2mat([[10, 7, 11, 10, 14], [1, 1, 13, 3, 2], [6, 13, 3, 2, 6],
[10, 10, 12, 1, 2], [2, 1, 5, 7, 10]])
b1 = list2vec([1, 1, -1, -1, 1])
A2 = Mat((set(range(97,123)),set(range(65,91))),{(x,y): 301-(7*((x-97)+26*(y
-65))%761) for x in range(97,123) for y in range(65,91)})
b2 = Vec(A2.D[0], {x:1 for x in A2.D[0]})
w1 = Vec(A1.D[1], {x:-2 for x in A1.D[1]})
print(A1 * w1 - b1)
print(find_grad(A1, b1, Vec(A1.D[1], {})))


## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    grad = find_grad(A,b,w)
    w_ = w - sigma * grad
    return w_
    

