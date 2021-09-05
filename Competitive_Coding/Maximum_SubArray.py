# Dictionary based Simple method

def subArrayExists(self,arr,n):
        if 0 in arr:
            return True
        if len(arr)==0:
            return False
        else:
            width = n
            left = 0
            while (width > 0):
                if (sum(arr[left:left+width]) == 0):
                    #print(arr[left:left+width])
                    return True
                else:
                    for i in range(0,n - width+1):
                        #print(arr[i:i+width])
                        if (sum(arr[i:i+width]) == 0):
                            return True
                    width -= 1 

# Fast Algorithm

def subArrayExists(arr,n):
	if 0 in arr:
		return True
    if len(arr)==0:
        return False
    else:
    	sub = set()
    	sum_val = 0

    	for i in range(n):
    		sum_val += arr[i]
    		if (sum_val == 0) or (sum_val in sub):
    			return True
    		sub.add(sum_val)
    	return False

