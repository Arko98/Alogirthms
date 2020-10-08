import numpy as np
import numpy.linalg as LA

def proj(v1,v2):
  '''
  Function to compute projection of v2 on v1
  '''
  alpha = np.dot(v1,v2)/np.dot(v1,v1)                                                  # proj(a,b) = aTb/aTa
  return alpha

def Gram_Schmid(M):
  '''
  Given any (m x n) matrix,M this function computers corresponding orthonormal matrix B such that,
  1. BTB = I
  2. C(M) = C(B) i.e Columnspace will be same
  '''
  row,col = M.shape
  Q = []                                                                               # List to append all orthogonal column vector later to be normalized
  for c in range(col):
    column_vector = M[:,c]    
    if c == 0:                                                                         # First column vector is itself taken to be orthogonal hence append
      Q.append(column_vector)
    else:
      for ortho_col_vec in Q:                                                          # For all previous orthogonal column vectors do operation on current column vector
        temp_col_vec = column_vector.copy()
        column_vector -= np.multiply(proj(ortho_col_vec,temp_col_vec),ortho_col_vec)   # B = B - proj(A,B)*A for all A in Q
      if (LA.norm(column_vector)!=0):                                                  # If column vector is linearly independent then add to Q
        Q.append(column_vector)
  # Orthonormalizartion of Q
  B = []                                                                               # Output Orthonormalized Matrix
  for col_vec in Q:
    B.append(col_vec/LA.norm(col_vec))
  return np.array(B).T



A = np.array([[1,1],
              [1,0],
              [1,2]],dtype=np.float32)



B = Gram_Schmid(A)
print(B)
print(np.matmul(B.T,B))
