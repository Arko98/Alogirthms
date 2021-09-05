# Problem URL: https://leetcode.com/problems/unique-paths

class Solution:
    def solve(self, i: int, j: int, memo_table: List[List[int]]):
        if memo_table[i][j] == 0:
            memo_table[i][j] = memo_table[i-1][j] + memo_table[i][j-1]
    
    def uniquePaths(self, m: int, n: int) -> int:
        memo_table = [[0 for i in range(n)] for j in range(m)]
        # Initialization
        for row in range(m):
            memo_table[row][0] = 1
        for col in range(n):
            memo_table[0][col] = 1
        
        # Iteration
        for i in range(1,m):
            for j in range(1,n):
                self.solve(i,j,memo_table)
        
        return memo_table[m-1][n-1]