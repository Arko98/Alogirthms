def Partition(Array,left,right):
  '''
  Partition function to sort the array with respect to the pivot
  '''
  pivot = Array[right]
  i = left-1
  for j in range(left,right,1):
    if (Array[j] < pivot):
      i += 1
      Array[i],Array[j] = Array[j],Array[i]
  Array[i+1],Array[right] = Array[right],Array[i+1]
  return i+1

def Find_Small_K(Array, left, right, k):
  '''
  Fast Algorithm to find kth smallest element in unsorted array
  Brute Force: O(n^2)
  Optimized : O(logn)
  '''
  if (left == right):
    return Array[left]
  q = Partition(Array,left,right)
  L_Sub_Len = q-left+1
  if (k==L_Sub_Len):
    return Array[q]
  elif (k < L_Sub_Len):
    return Find_Small_K(Array,left,q-1,k)
  else:
    return Find_Small_K(Array,q+1,right,k-L_Sub_Len)

# Driver Code
A = [1, 4, 6, 8, 7, 2, 5, 3]
K = 4
print(Find_Small_K(A,0,len(A)-1,K))
