def Binary_Search (array,x):
  begin = 0
  end = len(array)
  while begin<=end:
    mid = (begin + end)//2
    if (x == array[mid]):
      return mid
    elif (x > array[mid]):
      begin = mid+1
    elif (x < array[mid]):
      end = mid-1
  return (-1)

array = [1,24,7,36,94,13,34,79,14,63,89]
X = 79
res = Binary_Search(sorted(array),X)
print("Sorted Array: {}".format(sorted(array)))
print("Position of Element in Array: {}".format(res))
