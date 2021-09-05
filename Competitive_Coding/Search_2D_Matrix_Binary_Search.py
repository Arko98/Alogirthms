# Problem URL: https://leetcode.com/problems/search-a-2d-matrix

class Solution:
    def binarySearch(self, array, begin, end, target):
        mid = (begin + end)//2 
        while begin<=end:
            if array[mid] == target:
                return True
            elif array[mid] < target:
                begin = mid + 1
                return self.binarySearch(array,begin,end,target)
            else:
                end = mid - 1
                return self.binarySearch(array,begin,end,target)
        return False
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            if target>= matrix[row][0] and target<= matrix[row][cols-1]:
                return self.binarySearch(matrix[row],0,cols-1,target)
        return False