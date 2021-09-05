# Problem URL: https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        flag = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= flag:
                flag = 1
            else:
                flag += 1
        if flag == 1:
            return True
        return False
            