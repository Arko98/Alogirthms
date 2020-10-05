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

def difference(Array):
  '''
  Function to Calculate Difference of elements from first element
  '''
  Diff_Array = []
  for i in range(1,len(Array)):
    Diff_Array.append(abs(Array[i]-Array[0]))
  #print(Diff_Array)
  return Diff_Array

def compare(Main_Array,Array,Kth_Small):
  '''
  Compare distances According to Kth Smallest Distance
  And add the corresponding element from main array in
  final output array
  '''
  print("In Compare")
  final_list = []
  print(Main_Array)
  print(Array)
  for i in range(0,len(Array)):
    if (Array[i]<=Kth_Small):
      final_list.append(Main_Array[i+1])
  return final_list

def Find_K_Smalls(Array,K):
  '''
  Complete Algorithm O(n)
  1. Difference O(n)
  2. Quick Select O(n)
  3. Compare and Output O(n)
  '''
  diff_array = difference(Array)
  diff_copy = diff_array.copy()
  Kth_Small = Find_Small_K(diff_copy,0,len(diff_array)-1,K)
  #print(Kth_Small)
  Final_List = compare(Array,diff_array,Kth_Small)
  return Final_List

# Driver Code
A = [8, 3, 19, -2, 17, 40, 6, 25]
K = 4
Final_Output = Find_K_Smalls(A,K)
print(Final_Output)
