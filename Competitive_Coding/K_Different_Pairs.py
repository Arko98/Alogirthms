# Problem: https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = []
        for i in range(len(nums)):
            if nums[i]+k in nums[i+1:]:
                print('yes')
                tuple_obj = None
                if nums[i] <= nums[i]+k:
                    tuple_obj = (nums[i],nums[i]+k)
                else:
                    tuple_obj = (nums[i]+k, nums[i])
                ans.append(tuple_obj)
            if nums[i]-k in nums[i+1:]:
                print('yes')
                tuple_obj = None
                if nums[i] <= nums[i]-k:
                    tuple_obj = (nums[i],nums[i]-k)
                else:
                    tuple_obj = (nums[i]-k, nums[i])
                ans.append(tuple_obj)
        print(set(ans))
        return len(set(ans))
