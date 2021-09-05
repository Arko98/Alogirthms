# Problem URL: https://leetcode.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = set()
        nums.sort()
        if len(nums) < 4:
            return []
            
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                p = j+1
                q = len(nums)-1
                while p < q:
                    if (nums[i]+nums[j] == target - (nums[p]+nums[q])):
                        solution.add((nums[i], nums[j], nums[p], nums[q]))
                        p += 1
                        q -= 1
                    elif (nums[i]+nums[j] > target - (nums[p]+nums[q])):
                        q -= 1
                    else:
                        p += 1
                    
        return (solution)