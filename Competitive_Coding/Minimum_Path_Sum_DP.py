# Problem URL: https://leetcode.com/problems/minimum-path-sum

class Solution: 
    
    def solve(self, i, j, grid, memo_table):
        memo_table[i][j] = grid[i][j] + min(memo_table[i-1][j],memo_table[i][j-1])

    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo_table = [[0 for i in range(cols)] for j in range(rows)]
        
        # Row Initialization
        for i in range(cols):
            if i == 0:
                memo_table[0][i] = grid[0][i]
            else:
                memo_table[0][i] = sum(grid[0][:i+1])
                
        # Column Initialization
        for j in range(rows):
            if j == 0:
                memo_table[j][0] = grid[j][0]
            else:
                memo_table[j][0] = sum([row[0] for row in grid][:j+1])

        # Calling Function
        for i in range(1,rows):
            for j in range(1,cols):
                self.solve(i,j,grid,memo_table)
        
        return memo_table[rows-1][cols-1]