# Problem URL: https://leetcode.com/problems/spiral-matrix/

def spiral(matrix):
	result = []
	while matrix:
		result += matrix.pop(0)
		matrix = list(zip(*matrix))[::-1]

	return result