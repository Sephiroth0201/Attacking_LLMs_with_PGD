import math
import numpy as np

def to_tableau(c, A, b):
    xb = [eq + [x] for eq, x in zip(A, b)]
    z = c + [0]
    return xb + [z]

def get_pivot_position(tableau):
    z = tableau[-1]
    column = next(i for i, x in enumerate(z[:-1]) if x > 0)

    restrictions = []
    for eq in tableau[:-1]:
        el = eq[column]
        restrictions.append(math.inf if el <= 0 else eq[-1] / el)

    row = restrictions.index(min(restrictions))
    return row, column

def pivot_step(tableau, pivot_position):
    new_tableau = [[] for eq in tableau]

    i, j = pivot_position
    pivot_value = tableau[i][j]
    new_tableau[i] = np.array(tableau[i]) / pivot_value

    for eq_i, eq in enumerate(tableau):
        if eq_i != i:
            multiplier = np.array(new_tableau[i]) * tableau[eq_i][j]
            new_tableau[eq_i] = np.array(tableau[eq_i]) - multiplier

    return new_tableau

def is_basic(column):
    return sum(column) == 1 and len([c for c in column if c == 0]) == len(column) - 1

def get_solution(tableau):
    columns = np.array(tableau).T
    solutions = []
    for column in columns[:-1]:
        solution = 0
        if is_basic(column):
            one_index = column.tolist().index(1)
            solution = columns[-1][one_index]
        solutions.append(solution)

    return solutions

def can_be_improved(tableau):
    z = tableau[-1]
    return any(x < 0 for x in z[:-1])

def simplex(c, A, b):
    tableau = to_tableau(c, A, b)

    while can_be_improved(tableau):
        pivot_position = get_pivot_position(tableau)
        tableau = pivot_step(tableau, pivot_position)

    return tableau,get_solution(tableau)

def get_vector(prompt):
    vector_str = input(prompt).strip()
    return list(map(int, vector_str.split()))

def get_matrix(prompt, rows, cols):
    print(prompt)
    matrix = []
    for i in range(rows):
        row = get_vector(f"Enter row {i+1} separated by spaces: ")
        if len(row) != cols:
            print(f"Error: Row {i+1} should have {cols} elements.")
            return None
        matrix.append(row)
    return matrix


#getting user input
c = get_vector("Enter the vector c separated by spaces: ")
A = get_matrix("Enter the matrix A:", 2, 3)
b = get_vector("Enter the vector b separated by spaces: ")

#print(simplex(c,A,b)[0])
print(simplex(c,A,b)[1])
