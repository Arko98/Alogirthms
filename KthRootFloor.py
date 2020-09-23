def POW(n,k):
  '''
  Fast Recursive O(logn) algorithm for computing n^k
  '''
  if k==0:
    return 1
  elif k==1:
    return n
  pow_val = POW(n,k//2)
  if (k%2==0):  # If k is even then x^n = x^(n/2)*x^(n/2)
    return pow_val*pow_val
  else:         # If k is odd then x^n = x*x^(floor(n/2))*x^(floor(n/2))
    return n*pow_val*pow_val

def Search(left,right,n,k):
  '''
  Fast Algorithm to find floor(n**(1/k)) in O(logn) using O(logn) Power Raiser
  '''
  if (left<=right):
    mid = (left+right)//2
    if (POW(mid,k)<=n and POW(mid+1,k)>N):
      return mid
    elif (POW(mid,k)<n):
      left = mid+1
      return Search(left,right,n,k)
    right = mid-1
    return Search(left,right,n,k)
  return left

# driver code
N = 10
K = 5
print(Search(0,N,N,K))
