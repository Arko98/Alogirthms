'''
This Code transforms a matrix into Row Reduced Echelon Form using the Row Echelon Form of a matrix
Stage : Developmental
Many test cases are checked, yet to check some corner cases. If you notice a corner case that gives
error, please create a branch and update accordingly
or mail me at: de.arkadipta05@gmail.com, ai20mtech14002@iith.ac.in , arkadipta.de@gcettb.ac.in 
'''

import numpy as np

def Row_Echelon(A): 
  '''
  Function to transform a matrix into Row-Echelon Form
  '''
  row = A.shape[0]
  col = A.shape[1]
  max_piv_pos = min(row,col)            #p = min(row_num,col_num), then (p,p) will be pivot, no need to check sizes 
  for i in range(max_piv_pos):
    pivot = A[i,i]
    if (pivot == 0):                    #Ignore for 0 pivot
      continue
    A[i] = A[i]/pivot                   #Normalize Pivot, so that pivot = 1
    for j in range(i+1,A.shape[0],1):
      A[j] = A[j] - A[j,i]*A[i]         #Row_j = Row_j - (element below pivot)*Pivot_row to make all 0's below pivot
  return A


def Reduced_Row_Echelon_Form(A):
  '''
  Function to transform a matrix into Reduced-Row-Echelon Form
  Process: 1) Make A Row-Echelon
           2) From last pivot make all elements above the pivot in the column 0's
  '''
  A = Row_Echelon(A)
  for i in range(max_piv_pos-1,0,-1):
    pivot = A[i,i]
    if (pivot == 0):                   #Ignore for 0 pivot
      continue
    for j in range(i-1,-1,-1):
      A[j] = A[j] - A[j,i]*A[i]        #Row_j = Row_j - (element below pivot)*Pivot_row to make all 0's above pivot
  return A

#Test Cases:
'''
A = np.array([[3,4,5], 
              [2,0,4], 
              [1,0,12]], dtype = np.float)
'''
'''
A = np.array([[2,1,3,6],
              [1,5,6,4],
              [4,3,2,5]],dtype = np.float) 
'''

A = np.array([[2,1,3],
              [1,5,6],
              [4,3,2],
              [6,0,3]],dtype = np.float)


'''
A = np.array([[2,1,3],
              [1,5,6],
              [4,2,6]],dtype = np.float)
'''

RE = Row_Echelon(A)
print('Row Echelon Form = \n',RE)
RRE = Reduced_Row_Echelon_Form(A)
print('\nReduced Row Echelon Form = \n',RRE)
