# Problem URL: https://leetcode.com/problems/search-insert-position

class Solution:
    def binarySearch(self, nums: List[int], start: int, end: int, target: int) -> int:
        # Base Case
        mid = (start + end)//2
        while (start <= end):
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
                return self.binarySearch(nums, start, end, target)
            elif nums[mid] > target:
                end = mid - 1
                return self.binarySearch(nums, start, end, target)
        # If not found
        if (start>end):
            return start
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums)-1, target)
            