def maximum_subarray_sum(array):
	max_so_far = -10**7
	max_end_here = 0
	for i in range(len(array)-1):
		max_end_here += array[i]
		if max_so_far < max_end_here:
			max_so_far = max_end_here
		if max_end_here < 0:
			max_end_here = 0
	return max_so_far