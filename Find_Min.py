def find_min(array,left,right):
  '''
  Function to find minimum element in a decreasing and 
  then increasing sequence in O(logn) time
  '''
  if (left<=right):
    mid = (left + right)//2
    if (array[mid]<array[mid+1] and array[mid]<array[mid-1]):
      return array[mid]
    elif (array[mid]>array[mid+1]):
      left = mid+1
      return find_min(array,left,right)
    right = mid-1
    return find_min(array,left,right)

A = [43,41,33,27,13,8,6,2,5,7,21,55]
print(find_min(A,0,len(A)-1))
