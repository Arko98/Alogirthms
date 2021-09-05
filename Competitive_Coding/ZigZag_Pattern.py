# Problem URL: https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        string = [i for i in s]
        table = [['' for i in range(len(string))] for j in range(numRows)]
        string_idx = 0
        row = 0
        col = 0
        if numRows == 1:
            return s
        else:
            while (string_idx < len(string)):
                for i in range(row, numRows):
                    if (string_idx < len(string)):
                        print('if for ',row,col,string_idx)
                        table[row][col] = string[string_idx]
                        row += 1
                        string_idx += 1
                if row == numRows:
                    col += 1
                    for i in range(numRows-2,-1,-1):
                        row = i
                        print('elif for ',row,col,string_idx)
                        if (string_idx < len(string)):
                            table[row][col] = string[string_idx]
                            string_idx += 1
                            if (i>0):
                                col += 1
                    row = 1
                
        output_string = ''
        for i in range(len(table)):
            for j in range(len(table[0])):
                if table[i][j] != '':
                    output_string += table[i][j]
                    
        return output_string
                