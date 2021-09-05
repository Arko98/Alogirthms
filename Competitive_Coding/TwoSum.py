#Problem URL: https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out_list = []
        for i in range(len(nums)):
            if (target - nums[i] in nums and nums.index(target - nums[i]) != i):
                out_list.append(i)
                out_list.append(nums.index(target - nums[i]))
                break
        return out_list