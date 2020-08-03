import numpy as np

def getminor(mat,temp,n,p,q):
  i,j = 0,0
  for row in range(n):
    for col in range(n):
      if (row!=p and col!=q):
        temp[i][j] = mat[row][col]
        j += 1
        if (j==n-1):
          j = 0
          i = i+1
  return temp

def determinant(mat,n):
  D = 0
  sign = 1
  temp = [[0,0,0,0], 
          [0,0,0,0], 
          [0,0,0,0], 
          [0,0,0,0]]
  if (n==1):
    return mat[0][0]
  for f in range(n):
    temp = getminor(mat,temp,n,0,f)
    D += sign*mat[0][f]*determinant(temp,n-1)
    sign = -sign
  return D

N = 4
matrix = [[1, 0, 2, -1], 
          [3, 0, 0, 5 ], 
          [2, 1, 4, -3], 
          [1, 0, 5, 0 ]]
matrix = np.array(matrix)
print("Determinant of the matrix is : {}".format(determinant(matrix, N)))
