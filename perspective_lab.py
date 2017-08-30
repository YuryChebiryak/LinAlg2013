from image_mat_util import *

from mat import Mat
from vec import Vec
from matutil import *

from solver import solve

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    y1 = v['y1']
    y2 = v['y2']
    y3 = v['y3']
    return Vec({'y1','y2','y3'}, {'y1':y1/y3, 'y2':y2/y3, 'y3':1})

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):w1*x1, ('y3','x2'):w1*x2, ('y3','x3'):w1, ('y1','x1'):-x1, ('y1','x2'):-x2, ('y1','x3'):-1 })
    v = Vec(domain, {('y3','x1'):w2*x1, ('y3','x2'):w2*x2, ('y3','x3'):w2, ('y2','x1'):-x1, ('y2','x2'):-x2, ('y2','x3'):-1 } )
    return [u, v]


## Task 3
domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
ungr = Vec( domain, { ('y1','x1'): 1 } )
#L = Mat( ( {0,1,2,3,4,5,6,7,8}, domain), 0
vecs= make_equations(358,36,0,0) + make_equations(329, 597, 0, 1) + make_equations(592, 157, 1, 0) + make_equations(580, 483, 1, 1) + [ ungr ];
L = rowdict2mat(vecs)
print ("L = ", L)
b = Vec( { x for x in range(9) }, {8:1} )
print(" b= ", b)
h = solve(L, b)
print ("h res = ", (L * h) * (L * h))
print("h ",h)
print("L*h = ", L*h)
H = Mat(({'y1', 'y2', 'y3'}, {'x1', 'x2', 'x3'}), h.f)
print("H=", H)

(X_pts, colors) = file2mat('board.png', ('x1','x2','x3'))
Y_pts = H * X_pts

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    d = mat2coldict(Y)
    W = { x:move2board(d[x]) for x in d.keys() } 
    return coldict2mat(W)

Y_board = mat_move2board(Y_pts)
mat2display(Y_board, colors, ('y1','y2','y3'), scale=1000, xmin =None, ymin=None)

