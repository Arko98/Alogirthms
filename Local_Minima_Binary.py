def local_minima(left,right,array):
  '''
  Function to calculate local minima using binary search technique
  '''
  mid = int((left+right)/2)
  if (mid == 0 or array[mid]<array[mid-1] and mid == len(array)-1 or array[mid]<array[mid+1]):
    return array[mid]
  elif (mid > 0 and array[mid]>array[mid-1]):
    right = mid-1
    return local_minima(left,right,array)
  left = mid+1
  return local_minima(left,right,array)

A = [4, 33, 14, 29, 5, 40]
left = 0
right = len(A)-1
print(local_minima(left,right,A))
