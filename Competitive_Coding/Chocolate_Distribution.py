def find_min_diff(arr,n,m):
	arr.sort()
	min_diff = 10**7
	for i in range(n-m+1):
		min_diff = min(min_diff,arr[i+m]-arr[i])
	return min_diff