#load library
import numpy as np

#create a matrix
matrix = np.array([[1,2],
                    [1,2],
                    [1,2]])
print(matrix)

# create a matrix we can use NumPy two-dimensional array
# NumPy two-dimensional array is a matrix
# This is not recommended
matrix_object = np.asmatrix([[1,2],
                         [1,2],
                         [1,2]])

print(matrix_object)