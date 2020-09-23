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

print(POW(5,10))
