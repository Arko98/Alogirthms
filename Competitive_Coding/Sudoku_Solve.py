# Problem URL: https://leetcode.com/problems/sudoku-solver

class Solution:
    def find_empty_loc(self, board, location_list):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    location_list[0] = row
                    location_list[1] = col
                    return True
        return False
    
    def not_safe_row(self, board, row, num):
        for col in range(9):
            if board[row][col] == num:
                return True
        return False
    
    def not_safe_col(self, board, col, num):
        for row in range(len(board)):
            if board[row][col] == num:
                return True
        return False
    
    def not_safe_sub_board(self, board, row, col, num):
        for i in range(3):
            for j in range(3):
                if board[i + row][j + col] == num:
                    return True
        return False
    
    def check_safe(self, board, row, col, num):
        return (not self.not_safe_row(board,row,num) and not self.not_safe_col(board,col,num) and not self.not_safe_sub_board(board, row - row%3, col - col%3, num))
    
    def solver(self, board):
        candidates = ["1","2","3","4","5","6","7","8","9"]
        location_list = [0,0]
        
        # Find Empty Space
        if self.find_empty_loc(board,location_list) == False:
            return True
        
        # If Empty Space Found get location
        row = location_list[0]
        col = location_list[1]
        
        for i in candidates:
            # Check Safety of Assignmemt before assigning candidate
            if self.check_safe(board, row, col, i) == True:
                # If assignment is safe then make aassignment
                board[row][col] = i
                # Check solveability after assignment
                if self.solver(board) == True:
                    return True
                # If not solvable, reverse back and try again
                board[row][col] = "."
        return False
    
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        flag = self.solver(board)
        print(board)