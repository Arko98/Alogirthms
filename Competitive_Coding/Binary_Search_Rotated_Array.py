# Problem URL: https://leetcode.com/problems/search-in-rotated-sorted-array-ii

class Solution:
    def binarySearch(self, array, begin, end, target):
        mid = (begin + end)//2
        while (begin<=end):
            if array[mid] == target:
                return True
            elif array[mid] < target:
                begin = mid + 1
                return self.binarySearch(array,begin,end,target)
            else:
                end = mid - 1
                return self.binarySearch(array,begin,end,target)
        return False
    
    def search(self, nums: List[int], target: int) -> bool:
        array = nums.copy()
        pivot = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                pivot = i
                break
        if pivot != 0:
            array = nums[pivot:]
            array.extend(nums[:pivot])
        return self.binarySearch(array,0,len(nums)-1,target)