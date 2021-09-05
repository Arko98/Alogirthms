# Problem URL: https://leetcode.com/problems/maximum-subarray/

def solve(array):
	current_sum = 0
	max_sum = array[0]

	for i in array:
		current_sum = max(current_sum + n, n)
		max_sum = max(current_sum, max_sum)

	return max_sum