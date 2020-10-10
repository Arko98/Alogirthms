def find_index(Array,left,right):
  '''
  Function to find A[i]=i in O(logn)
  '''
  mid = (left+right)//2
  if (Array[mid]==mid):
    return Array[mid]
  elif (Array[mid]<mid):
    # Go to Right Subarray
    return find_index(Array,mid+1,right)
  elif (Array[mid]>mid):
    return find_index(Array,left,mid-1)
  return -1
  
# Driver Code
A = [-1,0,1,3,5,12,45]
print(find_index(A,0,len(A)-1))
