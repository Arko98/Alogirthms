import math
global base
base = 10

def pow(x,y):
  '''
  Fast Algorithm to raise x^y in O(logn)
  '''
  if (y==0):
    return 1
  elif (y==1):
    return x
  else:
    temp = pow(x,y//2)
    if (y%2 == 0):
      return temp*temp
    else:
      return x*temp*temp

def encode(Sequence):
  '''
  Function to Encode String with positional Encoding
  '''
  value = 0
  for i in range(len(Sequence)):
    value += (ord(Sequence[i])-96)*pow(base,len(Sequence)-1-i)
  return value

def Rabin_Karp(Text,Pattern):
  '''
  Rabin Karp Algorithm for fast string matching in O(m+n)
  '''
  Text = [i for i in Text]
  Pattern = [i for i in Pattern]
  m = len(Text)
  n = len(Pattern)

  hash_P = encode(Pattern)
  hash_T = encode(Text[:n])

  for i in range(m-n+1):
    if (i == 0):
       if (hash_P == hash_T):
        return i
    else:
      i_prev = i-1
      hash_T = base*(hash_T - (ord(Text[i_prev])-96)*pow(base,n-1)) + (ord(Text[i_prev+n])-96)
      if (hash_P == hash_T):
        return i
  return -1

# Driver Code
Text = 'weljrjhkfnabcdakjsdh'
Pattern = 'abcd'

position = Rabin_Karp(Text,Pattern)
if (position != -1):
  print("Pattern found at {} index".format(position))
else:
  print("Pattern not found")
