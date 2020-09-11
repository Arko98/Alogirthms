global Neg_INF
Neg_INF = -100000

def max_subarray(Array):  
  max_so_far = 0
  max_end = Neg_INF
  for i in range(len(Array)):
    max_end += Array[i]
    if (max_end > max_so_far):
      max_so_far = max_end
    if (max_end<0):
      max_end = 0
  return max_so_far

# Driver Code
A = [1, 4, 6, 8, 7, 2, -2, 3]
print(max_subarray(A))
