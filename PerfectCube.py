def PerfectCube(Array,left,right,x):
  '''
  Fast O(logn) algorithm to find check if an element is perfect cube or not
  '''
  if (right<left):
    return 'No'
  else:
    mid = (left+right)//2
    if (x**(1/3)==Array[mid]):
      return 'Yes'
    elif (x**(1/3)<Array[mid]):
      return PerfectCube(Array,left,mid-1,x)
    else:
      return PerfectCube(Array,mid+1,right,x)

A = [i for i in range(0,10000)]
n = 
print(PerfectCube(A,0,len(A)-1,n))

'''
Alternative Fast Algorithm
def is_perfect_cube(number):
  number = abs(number)
  return round(number**(1 / 3))**3==number
'''
