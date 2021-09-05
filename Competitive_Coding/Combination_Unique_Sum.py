# Problem URL: https://leetcode.com/problems/combination-sum-ii

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        
        def backtrack(nums, result, target):
            if target<0:
                return
            if target == 0:
                ans.append(result)
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[i+1:], result + [nums[i]], target - nums[i])
            
        backtrack(candidates, [], target)
        return ans