Problem URL: https://leetcode.com/problems/unique-paths-ii

class Solution:
    def solve(self, i, j, obstracleGrid, memo_table):
        if obstracleGrid[i][j] == 1:
            memo_table[i][j] = 0
        else:
            memo_table[i][j] = memo_table[i-1][j] + memo_table[i][j-1]
        
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # Base Case
        if obstacleGrid[0][0] == 1:
            return 0
        
        # Memo Table
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo_table = [[0 for i in range(n)] for j in range(m)]
        
        # Initialization
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                memo_table[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                memo_table[0][j] = 1
        
        # Iterations
        for i in range(1,m):
            for j in range(1,n):
                self.solve(i,j,obstacleGrid,memo_table)
                
        print(memo_table)       
        return memo_table[m-1][n-1]