def Partition(Array,left,right):
  '''
  Partition function to sort the array with respect to the pivot
  '''
  pivot = Array[right]
  i = left-1
  for j in range(left,right,1):
    if (Array[j]< pivot):
      i += 1
      Array[i],Array[j] = Array[j],Array[i]
  Array[i+1],Array[right] = Array[right],Array[i+1]
  return i+1

def Quicksort(Array,left,right):
  '''
  Main Quicksort function
  '''
  if (left < right):
    q = Partition(Array,left,right)
    Quicksort(Array,left,q-1)
    Quicksort(Array,q+1,right)

# Driver Code
A = [1, 4, 6, 8, 7, 2, 5, 3]
Quicksort(A,0,len(A)-1)
print(A)
