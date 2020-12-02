def Least_Recently_Used(Cache,Request,History):
  '''
  Page Replacement Greedy Algorithm for minimum Cache Miss
  '''
  if (Request in Cache):
    print('Cache Hit')
    print('Cache State:')
    print(Cache)
  else:
    if (len(History) == 0):
      print('Cache Miss on first request')
      Cache[0] = Request
    elif (len(History) != 0):
      print(History)
      print('Cache Miss')
      min_idx_list = []
      for i in Cache:
        min_index = 1000
        for j in range(len(History)-1,-1,-1):
          if (i == History[j]):
            if (j < min_index):
              min_index = j
              min_idx_list.append((i,min_index))
              break
      min_idx_list = sorted(min_idx_list,key = lambda x:x[1])
      print(min_idx_list)
      Cache[Cache.index(min_idx_list[0][0])] = Request
    print('Cache State:')
    print(Cache)

# Driver Code
cache = [1,2,3,4]               # Input Required Cache Here
request = int(input())
history = []
while (request != -1):
  Least_Recently_Used(cache,request,history)
  history.append(request)
  request = int(input())
