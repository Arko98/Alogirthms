# Problem URL: https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        solution = []
        nums.sort()
        closest = -1
        difference = float("inf")
        
        for i in range(len(nums)-2):
            a = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                current_sum = a+b+c
                if current_sum == target:
                    return target
                if (abs(target - current_sum) < difference):
                    difference = abs(target - current_sum)
                    closest = current_sum
                if current_sum < target:
                    start += 1
                else:
                    end -= 1
        return closest