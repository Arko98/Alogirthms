# Problem Statement: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Cases
        if n==1:
            return 1
        if n==2:
            return 2
        
        # Memoization
        memo_table = [1]*(n+1)
        # Initialization
        memo_table[1] = 1
        memo_table[2] = 2
        # Iterative solution Memoization
        for i in range(3, n+1):
            memo_table[i] = memo_table[i-1]+memo_table[i-2]
        return memo_table[n]