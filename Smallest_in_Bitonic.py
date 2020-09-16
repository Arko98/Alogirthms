def Smallest_Bitonic(Array,left,right):
  '''
  Function to find smallest element in Bitonic Sequence in O(nlogn)
  '''
  if (left==right):
    return Array[left]
  mid = (left+right)//2
  if (Array[mid]>Array[mid+1]):
  # Smallest element will be in left side
    return Smallest_Bitonic(Array,mid+1,right)
  return Smallest_Bitonic(Array,left,mid-1)
  
# Driver Code
A = [4,5,6,5,3,1,2,3] # Bitonic Sequence
print(Smallest_Bitonic(A,0,len(A)-1)
