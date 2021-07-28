def merge(array, begin, mid, end):
    i = 0   
    j = 0 
    k = begin    
    
    n1 = mid - begin + 1
    n2 = end - mid
    L = [0]*(n1)
    R = [0]*(n2)
  
    for a in range(n1):
        L[a] = array[begin + a]
    for a in range(n2):
        R[a] = array[mid + 1 + a]
    
    while (i<n1 and j<n2):
        if (L[i] <= R[j]):
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while (j<n2):
        array[k] = R[j]
        j += 1
        k += 1
    while (i<n1):
        array[k] = L[i]
        i += 1
        k += 1

def mergesort(array, begin, end):
    if (begin < end):
        #mid = (begin + end)//2 
        mid = (begin + (end - 1)) // 2  # Same as line 35 but handles overflow
        mergesort(array, begin, mid)
        mergesort(array, mid+1, end)
        merge(array, begin, mid, end)
        
a = [2,8,5,1,4]
mergesort(a, 0, len(a)-1)
print(a)
