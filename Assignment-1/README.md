# Assignment 1
## Solving a linear programming problem with 3 variables x1,x2,x3 and 3 constraints.

The code performs the simplex procedure to maximise a given objective function c^Tx where c is a vector containing the coefficients.
This is subject to  the constraints Ax=b and x>=0. (given b>=0)

Stepwise explaination of the procedure:

### Making initial tableau
The function to_tableau forms the inital tableau with the augmented matrix A|b concatonated vertically with the array c +[0] making our objective function row

### Getting pivot row,column
To find the pivot column we find the largest positive element in our objective function row and the column it lies in is the pivot column.
Using the pivot column we divide each element in the last column by the corresponding element in the pivot column given that its positive and the minimum ratio thus obtained corresponds to the element in the pivot row.

### Pivot
now we perform row operations such that the pivot column has only one non zero element in the pivot row which is =1. (we use the pivot row to make all elements of the pivot column 0 except the one in the pivot row which is made to be 1)

### Optimality check
At the start of each iteration to check if the current tableau corresponds to the optimal tableau we check the last row for anyy positive elements, if there are no positive elements in the last row the current tableau is optimal.
We iterate until we find the optimal tableau and solution.

The code asks for user inputs for c,A,b as defined above.


