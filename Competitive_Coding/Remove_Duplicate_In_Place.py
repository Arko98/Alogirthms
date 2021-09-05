# Problem URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer = 1
        for i in range(1,len(nums)):
            if (nums[i] != nums[i-1]):
                nums[pointer] = nums[i]
                pointer +=1
        return pointer