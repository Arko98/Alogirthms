def minimum_steps(array,n,k):
	
	# If Array length is 0 or 1
	if len(array) <= 1:
		return 0

	# If Array is non-reachable
	if array[0] = 0:
		return -1

	max_reach = array[0]
	steps = array[0]
	jumps = 1

	for i in range(1,n):
		# Check if we have already reached array end
		if i == len(array) - 1:
			return jumps

		max_reach = max(max_reach, i + array[i])
		steps -= 1

		if steps == 0:
			jumps += 1
			if i >= max_reach:
				return -1

		steps = max_reach - i

	return -1