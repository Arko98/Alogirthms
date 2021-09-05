from collections import Counter

class Solution:
    def unique(self, row: List[str]) -> bool:
        counts = dict(Counter(row))
        for key in list(counts.keys()):
            if key != "." and counts[key] > 1:
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.unique(row) == False:
                return False
        
        for i in range(9):
            column = []
            for j in range(9):
                column.append(board[j][i])
            if self.unique(column) == False:
                return False
        
        i,j = 0,0
        for n in range(9):
            sub_board = []
            for x in range(i,i+3):
                for y in range(j,j+3):
                    # Check 3*3 sub-board
                    sub_board.append(board[x][y])
                    
            j += 3
            
            if (j > 8):
                i += 3
                j = 0
                
            if self.unique(sub_board) == False:
                return False
            
        return True