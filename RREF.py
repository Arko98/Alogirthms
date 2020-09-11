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
  row = A.shape[0]
  col = A.shape[1]
  max_piv_pos = min(row,col)           #p = min(row_num,col_num), then (p,p) will be pivot, no need to check sizes 
  for i in range(max_piv_pos-1,0,-1):
    pivot = A[i,i]
    if (pivot == 0):                   #Ignore for 0 pivot
      continue
    for j in range(i-1,-1,-1):
      A[j] = A[j] - A[j,i]*A[i]        #Row_j = Row_j - (element below pivot)*Pivot_row to make all 0's above pivot
  return A

def Inverse_Extract(RRE):
  '''
  Function to Extract Inverse Matrix from Augmented RRE of a Matrix
  Input: Augmented RRE Form of a Matrix
  '''
  row = A.shape[0]
  col = A.shape[1]
  Inv = np.zeros(shape = (int(col/2),int(col/2)),dtype = np.float)
  Inv_Col = 0
  for r in range(row):
    for c in range(int(col/2),col,+1):
      if(Inv_Col == int(col/2)):
        Inv_Col = 0
      Inv[r,Inv_Col] = RRE[r,c]
      Inv_Col += 1
  return Inv

# Driver Code

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
'''
A = np.array([[2,1,3],
              [1,5,6],
              [4,3,2],
              [6,0,3]],dtype = np.float)
'''
'''
A = np.array([[2,1,3],
              [1,5,6],
              [4,2,6]],dtype = np.float)
'''
'''
# Augmented Test Case for Inverse Evaluation
A = np.array([[2,1,3,1,0,0],
              [1,5,6,0,1,0],
              [4,3,2,0,0,1]],dtype = np.float)
''' 


RE = Row_Echelon(A)
print('Row Echelon Form = \n',RE)
RRE = Reduced_Row_Echelon_Form(A)
print('\nReduced Row Echelon Form = \n',RRE)
Inv = Inverse_Extract(RRE)        # Use only for Augmented test case else comment out             
print('\nInverse Matrix = \n',Inv)
