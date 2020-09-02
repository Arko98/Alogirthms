def find_bitonic_point(arr,left,right):
  '''
  Funtion to find the Bitonic point for a Bitonic Series
  Returns -1 if series is not bitonic 
  '''
  if (left <= right): 
    mid = (left+right) // 2
    if (arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
      return mid
    if (arr[mid]<arr[mid+1]):
      left = mid+1
      return find_bitonic_point(arr,left,right)
    else:
      right = mid-1
      return find_bitonic_point(arr,left,right)
  return -1
  
# Driver Code
A = [1,4,8,6,4,-1,-2]
left = 0
right = len(A)-1
print(find_bitonic_point(A,left,right))
