def max_subarray_cross(array,left,mid,right):
  # For left of mid
  inter_sum = 0
  left_sum = 0
  for i in range(mid-1,left-1,-1):
    inter_sum += array[i]
    if (inter_sum > left_sum):
      left_sum = inter_sum

  # For right of mid
  inter_sum = 0
  right_sum = 0
  for i in range(mid,right+1,1):
    inter_sum += array[i]
    if (inter_sum > right_sum):
      right_sum = inter_sum

  return max(right_sum + left_sum, left_sum, right_sum)

def max_subarray(array,left,right):
  if (left==right):
    return array[left]
  else:
    mid = (left+right)//2
    max_left = max_subarray(array,left,mid)
    max_right = max_subarray(array,mid+1,right)
    max_cross = max_subarray_cross(array,left,mid,right)
    return max(max_left,max_right,max_cross)

# Driver Code
A = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray(A,0,len(A)-1))
