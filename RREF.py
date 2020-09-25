'''
This Code transforms a matrix into Row Reduced Echelon Form using the Row Echelon Form of a matrix
Stage : Developmental
Many test cases are checked, yet to check some corner cases. If you notice a corner case that gives
error, please create a branch and update accordingly
or mail me at: de.arkadipta05@gmail.com, ai20mtech14002@iith.ac.in , arkadipta.de@gcettb.ac.in 

Author: Arkadipta De
'''
import numpy as np

def Row_Echelon(A): 
  '''
  Function to transform a matrix into Row-Echelon Form
  '''
  row = A.shape[0] 
  column = A.shape[1]

  if row==0 or column==0:
      return A
  for i in range(len(A)) :
      if A[i,0] !=0 :
          break
  else:
      A_Below = Row_Echelon(A[:,1:])
      return np.hstack([A[:,:1],A_Below])
  
  if i>0:
      ith_row = A[i].copy()
      A[i] = A[0]
      A[0] = ith_row 
    
  pivot = A[0,0]
  
  A[0] = A[0]/pivot                 #Normalize Pivot's Row
  A[1:] = A[1:] - A[0]*A[1:,0:1]    #Make Pivot Column 0

  A_Below = Row_Echelon(A[1:,1:])  
  A_Stacked = np.hstack([A[1:,:1],A_Below])
  return np.vstack([A[:1],A_Stacked])


def Reduced_Row_Echelon_Form(A):
  '''
  Function to transform a matrix into Reduced-Row-Echelon Form
  '''
  A = Row_Echelon(A)
  row = A.shape[0]-1
  col = A.shape[1]
  while (row > 0):
      i = row
      for j in range(col):
        if A[i,j]==1:
          while (i > 0):
            A[i-1] -= A[row]*A[i-1,j]
            i-=1
      row-=1
  return A

def Inverse(A):
  '''
  Function to Extract Inverse Matrix from Augmented RRE of a Matrix
  Input: Augmented RRE Form of a Matrix
  '''
  row = A.shape[0]
  col = A.shape[1]
  if (row!=col):
    print("\nInverse Does not exist")
  elif np.linalg.det(A)==0:
    print("\nInverse doesn't exist.")
  else:
    AI = np.hstack([A,np.identity(row)])
    AI_RREF = Reduced_Row_Echelon_Form(AI)
    AI_row = AI_RREF.shape[0]
    AI_col = AI_RREF.shape[1]
    return AI_RREF[:,int(AI_col/2):]
  
# Driver Code
A1 = np.array([[1,0,0],[0,1,0],[0,0,1]])
A2 = np.array([[0,0,1],[1,0,0],[0,1,0]])
A3 = np.array([[0,0,1,5],[0,1,2,1],[0,1,2,1]])
A4 = np.array([[1,3,1],[0,2,3],[34,-2,-1]])
A5 = np.array([[1,2,2],[-2,9,17],[1,0,0],[0,1,0]])
A6 = np.array([[1,1,1,1,1.0],[1,1,1,1,1],[1,1,1,1,1]])
A7 = np.array([[1,1,1,1,1.0],[1,1,2,2,2],[1,1,1,4,5]])
A8 = np.array([[1,1,1,1],[1,1,1,1],[1,2,3,4]])
A9 = np.array([[1,1,1],[1,1,2],[2,3,1]])

A = A5

RE = Row_Echelon(A)
print('Row Echelon Form = \n',RE)
RRE = Reduced_Row_Echelon_Form(A)
print('\nReduced Row Echelon Form = \n',RRE)
print("Inverse = \n",Inverse(A))  
