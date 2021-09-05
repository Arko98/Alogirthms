https://leetcode.com/problems/search-in-rotated-sorted-array

class Solution:
    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        mid = (start + end)//2
        while start <= end:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start += 1
                return self.binarySearch(nums, target, start, end)
            else:
                end -= 1
                return self.binarySearch(nums, target, start, end)
        if start>end:
            return -1
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        sorted_nums = []
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i
                break
        
        a = self.binarySearch(nums[pivot:], target, 0, len(nums[pivot:])-1)           # left sorted
        b = self.binarySearch(nums[:pivot], target, 0, len(nums[:pivot])-1)           # right sorted
        
        if a == -1 and b == -1:
            return -1
        elif a!=-1:
            return a+pivot
        else:
            return b