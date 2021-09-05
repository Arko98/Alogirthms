# Problem URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def binarySearch(self, nums: List[int], start: int, end: int, target: int) -> int:
        # Base Case
        mid = (start + end)//2
        while (start <= end):
            if nums[mid] == target:
                #return [mid]
                first = mid
                last = mid
                curr = mid
                while (curr-1 >= 0 and nums[curr-1] == target):
                    curr -= 1
                first = curr 
                while (curr+1 <= len(nums)-1 and nums[curr+1] == target):
                    curr += 1
                last = curr
                return [first,last]
            elif nums[mid] < target:
                start = mid + 1
                return self.binarySearch(nums, start, end, target)
            elif nums[mid] > target:
                end = mid - 1
                return self.binarySearch(nums, start, end, target)
        # If not found
        if (start > end):
            return ([-1,-1])
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self.binarySearch(nums, 0, len(nums) - 1, target)