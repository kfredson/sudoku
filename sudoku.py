import math, random
from cvxopt import solvers, matrix

#Define pre-set examples
preset = []
preset.append({(7, 3): None, (4, 7): None, (1, 3): None, (4, 8): None, (3, 0): 8, (2, 8): None, (8, 0): 1, (7, 8): 7, (5, 4): 9, (0, 7): None, (5, 6): None, (2, 6): None, (1, 6): 6, (5, 1): None, (3, 7): None, (0, 3): None, (8, 5): None, (2, 5): 4, (5, 8): 8, (4, 0): None, (1, 2): 4, (7, 4): None, (6, 4): None, (3, 3): 4, (2, 0): None, (8, 1): None, (7, 6): 9, (4, 4): 3, (6, 3): 5, (1, 5): None, (8, 8): 3, (7, 2): 5, (3, 6): 3, (2, 2): None, (7, 7): 2, (5, 7): 5, (5, 3): None, (4, 1): None, (1, 1): 7, (2, 7): None, (3, 2): None, (0, 0): 5, (6, 6): None, (5, 0): 7, (7, 1): None, (4, 5): None, (0, 4): 1, (5, 5): 1, (1, 4): None, (6, 0): None, (7, 5): None, (2, 3): 9, (2, 1): 8, (8, 7): None, (6, 8): None, (4, 2): 2, (1, 0): 2, (0, 8): 4, (6, 5): 3, (3, 5): None, (0, 1): None, (8, 3): None, (7, 0): None, (4, 6): 1, (6, 7): 1, (8, 6): None, (5, 2): 6, (6, 1): None, (3, 1): 1, (8, 2): None, (2, 4): None, (3, 8): 2, (0, 6): None, (1, 8): None, (6, 2): None, (4, 3): None, (1, 7): None, (0, 5): None, (3, 4): 6, (0, 2): None, (8, 4): 2})
preset.append({(7, 3): None, (4, 7): None, (1, 3): None, (4, 8): None, (3, 0): None, (2, 8): None, (8, 0): None, (7, 8): None, (5, 4): None, (0, 7): None, (5, 6): None, (2, 6): None, (1, 6): None, (5, 1): 9, (3, 7): None, (0, 3): None, (8, 5): None, (2, 5): None, (5, 8): None, (4, 0): None, (1, 2): None, (7, 4): 1, (6, 4): None, (3, 3): 5, (2, 0): None, (8, 1): None, (7, 6): None, (4, 4): None, (6, 3): None, (1, 5): 3, (8, 8): 9, (7, 2): 2, (3, 6): None, (2, 2): 1, (7, 7): None, (5, 7): None, (5, 3): None, (4, 1): None, (1, 1): None, (2, 7): None, (3, 2): None, (0, 0): None, (6, 6): None, (5, 0): None, (7, 1): None, (4, 5): None, (0, 4): None, (5, 5): None, (1, 4): None, (6, 0): 5, (7, 5): None, (2, 3): None, (2, 1): None, (8, 7): None, (6, 8): 3, (4, 2): 4, (1, 0): None, (0, 8): None, (6, 5): None, (3, 5): 7, (0, 1): None, (8, 3): None, (7, 0): None, (4, 6): 1, (6, 7): 7, (8, 6): None, (5, 2): None, (6, 1): None, (3, 1): None, (8, 2): None, (2, 4): 2, (3, 8): None, (0, 6): None, (1, 8): 5, (6, 2): None, (4, 3): None, (1, 7): 8, (0, 5): None, (3, 4): None, (0, 2): None, (8, 4): 4})
preset.append({(7, 3): None, (4, 7): None, (1, 3): None, (4, 8): None, (3, 0): None, (2, 8): None, (8, 0): None, (7, 8): None, (5, 4): None, (0, 7): None, (5, 6): 4, (2, 6): 2, (1, 6): None, (5, 1): None, (3, 7): None, (0, 3): 7, (8, 5): None, (2, 5): None, (5, 8): 8, (4, 0): None, (1, 2): None, (7, 4): None, (6, 4): 8, (3, 3): None, (2, 0): None, (8, 1): 4, (7, 6): None, (4, 4): None, (6, 3): None, (1, 5): None, (8, 8): None, (7, 2): 2, (3, 6): None, (2, 2): None, (7, 7): 5, (5, 7): 1, (5, 3): None, (4, 1): None, (1, 1): None, (2, 7): None, (3, 2): None, (0, 0): None, (6, 6): None, (5, 0): None, (7, 1): None, (4, 5): 9, (0, 4): None, (5, 5): None, (1, 4): None, (6, 0): None, (7, 5): None, (2, 3): 4, (2, 1): None, (8, 7): None, (6, 8): None, (4, 2): None, (1, 0): 1, (0, 8): None, (6, 5): 1, (3, 5): None, (0, 1): None, (8, 3): None, (7, 0): None, (4, 6): None, (6, 7): None, (8, 6): 3, (5, 2): None, (6, 1): None, (3, 1): None, (8, 2): None, (2, 4): 3, (3, 8): 6, (0, 6): None, (1, 8): None, (6, 2): None, (4, 3): 5, (1, 7): None, (0, 5): None, (3, 4): None, (0, 2): None, (8, 4): None})
preset.append({(7, 3): None, (4, 7): None, (1, 3): None, (4, 8): 2, (3, 0): None, (2, 8): None, (8, 0): None, (7, 8): 7, (5, 4): None, (0, 7): 9, (5, 6): None, (2, 6): 5, (1, 6): None, (5, 1): None, (3, 7): None, (0, 3): None, (8, 5): None, (2, 5): None, (5, 8): None, (4, 0): None, (1, 2): None, (7, 4): None, (6, 4): None, (3, 3): 3, (2, 0): None, (8, 1): None, (7, 6): None, (4, 4): 8, (6, 3): None, (1, 5): None, (8, 8): None, (7, 2): None, (3, 6): 9, (2, 2): 9, (7, 7): None, (5, 7): None, (5, 3): None, (4, 1): 1, (1, 1): 3, (2, 7): None, (3, 2): 5, (0, 0): 1, (6, 6): None, (5, 0): 6, (7, 1): 4, (4, 5): None, (0, 4): None, (5, 5): 4, (1, 4): 2, (6, 0): 3, (7, 5): None, (2, 3): 6, (2, 1): None, (8, 7): None, (6, 8): None, (4, 2): None, (1, 0): None, (0, 8): None, (6, 5): None, (3, 5): None, (0, 1): None, (8, 3): None, (7, 0): None, (4, 6): None, (6, 7): 1, (8, 6): 3, (5, 2): None, (6, 1): None, (3, 1): None, (8, 2): 7, (2, 4): None, (3, 8): None, (0, 6): None, (1, 8): 8, (6, 2): None, (4, 3): None, (1, 7): None, (0, 5): 7, (3, 4): None, (0, 2): None, (8, 4): None})
preset.append({(7, 3): None, (4, 7): 8, (1, 3): None, (4, 8): 9, (3, 0): None, (2, 8): None, (8, 0): 9, (7, 8): None, (5, 4): None, (0, 7): None, (5, 6): None, (2, 6): 2, (1, 6): None, (5, 1): None, (3, 7): None, (0, 3): None, (8, 5): None, (2, 5): None, (5, 8): None, (4, 0): 4, (1, 2): None, (7, 4): 5, (6, 4): 3, (3, 3): 4, (2, 0): None, (8, 1): None, (7, 6): None, (4, 4): None, (6, 3): None, (1, 5): None, (8, 8): 8, (7, 2): None, (3, 6): None, (2, 2): 3, (7, 7): 7, (5, 7): None, (5, 3): 6, (4, 1): 5, (1, 1): 2, (2, 7): None, (3, 2): None, (0, 0): 1, (6, 6): 6, (5, 0): None, (7, 1): 8, (4, 5): None, (0, 4): 4, (5, 5): 5, (1, 4): 6, (6, 0): None, (7, 5): None, (2, 3): None, (2, 1): None, (8, 7): None, (6, 8): None, (4, 2): 6, (1, 0): None, (0, 8): 6, (6, 5): None, (3, 5): 7, (0, 1): None, (8, 3): None, (7, 0): None, (4, 6): 7, (6, 7): None, (8, 6): None, (5, 2): None, (6, 1): None, (3, 1): None, (8, 2): None, (2, 4): 1, (3, 8): None, (0, 6): None, (1, 8): None, (6, 2): 7, (4, 3): None, (1, 7): 3, (0, 5): None, (3, 4): None, (0, 2): None, (8, 4): 7})


def print_board(board):
    for i in range(9):
        if (i%3==0):
            if i==3 or i==6:
                print '======================================='
            else:
                print '---------------------------------------'
        s = '|'
        for j in range(9):
            s = s + ' '
            if board[(i,j)] != None:
                s = s+str(board[(i,j)])
            else:
                s = s+ ' '
            if j%3==2 and j < 8:
                s = s+' ||'
            else:
                s = s+' |'
        print s
    print '---------------------------------------'


std_basis = []

#Create standard basis (1,0,0,0,0,0,0,0,0), (0,1,0,0,0,0,0,0,0), etc.
#(1,0,0,0,0,0,0,0,0) represents 1, (0,1,0,0,0,0,0,0,0) represents 2, ...
for i in range(9):
    curvec = []
    for j in range(9):
        if i==j:
            curvec.append(1.)
        else:
            curvec.append(0.)
    std_basis.append(curvec)

zeros = [0.,0.,0.,0.,0.,0.,0.,0.,0.]
ones = [1.,1.,1.,1.,1.,1.,1.,1.,1.]

#The sudoku will be represented by 81 nine-dimensional vectors,
#each vector will be a standard basis vector
#representing a single square with a number in it.
#The constraints are that vectors in each row, column and 3x3 square add up to
#the vector (1,1,1,1,1,1,1,1,1)
#All together the board is a 9x81=729 dimensional vector

board = dict()

choice = raw_input("Type E to enter your own board, or a number from 1-5 for a pre-set example: ")


#Get board from user input
if choice=='E':
    for i in range(9):
        for j in range(9):
            s = raw_input("Enter number in ("+str(i+1)+","+str(j+1)+") cell, 'x' for unknown: ")
            if (s != 'x'):
                num = int(s)
                if num < 1 or num > 9:
                    raise Exception("Must be integer between 1 and 9")
                board[(i,j)] = num
            else:
                board[(i,j)] = None
else:
    board = preset[int(choice)-1]

print "Trying to solve the board:"
print_board(board)
#print board

constraint_matrix = []
constraint_vector = []

#Create constraints

#Constraints enforcing only 1 number in each square
for i in range(81):
    curvec = []
    for j in range(81):
        if i==j:
            curvec.extend(ones)
        else:
            curvec.extend(zeros)
    if board[(math.floor(i/9),i%9)]!=None:
        constraint_vector.append(0.)
    else:
        constraint_vector.append(-1.)
    constraint_matrix.append(curvec)

#Row constraints
for k in range(9):
    for i in range(9):
        k_exists = 0
        curvec = []
        for j in range(81):
            if j >= 9*i and j < 9*(i+1):
                curvec.extend(std_basis[k])
                if board[(math.floor(j/9),j%9)]==k+1:
                    k_exists = 1
            else:
                curvec.extend(zeros)
        if k_exists==1:
            constraint_vector.append(0.)
        else:
            constraint_vector.append(-1.)
        constraint_matrix.append(curvec)    

#Column constraints
for k in range(9):
    for i in range(9):
        k_exists = 0
        curvec = []
        for j in range(81):
            if j%9 == i:
                curvec.extend(std_basis[k])
                if board[(math.floor(j/9),j%9)]==k+1:
                    k_exists = 1
            else:
                curvec.extend(zeros)
        if k_exists==1:
            constraint_vector.append(0.)
        else:
            constraint_vector.append(-1.)
        constraint_matrix.append(curvec)

#3x3 square constraints
for k in range(9):
    for i in range(9):
        curvec = []
        k_exists = 0
        for j in range(81):
            if math.floor(j/27)==math.floor(i/3) and math.floor((j%9)/3) == i%3:
                curvec.extend(std_basis[k])
                if board[(math.floor(j/9),j%9)]==k+1:
                    k_exists = 1
            else:
                curvec.extend(zeros)
        if k_exists==1:
            constraint_vector.append(0.)
        else:
            constraint_vector.append(-1.)
        constraint_matrix.append(curvec)

#Default solver for cvxopt requires that the rank of constraint matrix = its number of rows
#So we have to row reduce it.
#(GLPK solver does not require that but it's harder to install)
pivots = set()
for i in range(729):
    j = 0
    foundPivot = False 
    while j < len(constraint_matrix) and foundPivot==False:
        if constraint_matrix[j][i]!=0. and j not in pivots:
            pivots.add(j)
            foundPivot = True
            for k in range(len(constraint_matrix)):
                if k!=j and constraint_matrix[k][i] != 0.:
                    mult1 = constraint_matrix[j][i]
                    mult2 = constraint_matrix[k][i]
                    constraint_matrix[k] = [mult1*constraint_matrix[k][n]-mult2*constraint_matrix[j][n] for n in range(729)]
                    constraint_vector[k] = mult1*constraint_vector[k]-mult2*constraint_vector[j]
        j += 1

final_constraint_matrix = []
final_constraint_vector = []
for x in range(len(constraint_matrix)):
    if (min(constraint_matrix[x])!=0. or max(constraint_matrix[x])!=0.):
        final_constraint_matrix.append(constraint_matrix[x])
        final_constraint_vector.append(constraint_vector[x])

#Run linear program
num_tries = 0
solved=False
retry=True
max_tries = 1000
while num_tries<max_tries and solved==False and retry:
    #This will generate a random objective function
    #Very sloppy way to do this, but if we try enough different objective functions
    #we should eventually hit all the vertices of the solution polytope
    #and find an integer solution if there is one.
    c = [random.gauss(0,2) for x in range(729)]
    res = solvers.lp(matrix(final_constraint_vector),matrix(final_constraint_matrix),
                     matrix(c))

    solution = res['z']
    if type(solution)==type(None):
        #This means the solver thinks the problem is "infeasible" and there is no solution
        print "Could not find solution!  The solver thinks that a solution for this board does not exist."
        solved=False
        retry=False
    else:
        solved = True
        retry = True
        orig_board = board.copy()
        for x in range(81):
            total_sum = 0
            for y in range(9):
                if solution[9*x+y] > 0.6:
                    board[(math.floor(x/9),x%9)] = y+1
                total_sum += solution[9*x+y]
            if total_sum > 0.5 and board[(math.floor(x/9),x%9)]==None:
                solved = False
        if solved:
            print "The solver found this solution: "
            print_board(board)
            retry = False
        else:
            print "Found a solution but it is not an integer vector.  Retrying..."
            board = orig_board
    num_tries += 1

if solved==False and retry==True:
    print "Could not find a solution after "+str(max_tries)+" tries.  A solution may exist but we are giving up."
