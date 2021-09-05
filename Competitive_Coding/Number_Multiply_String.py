# Problem URL: https://leetcode.com/problems/multiply-strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit_map = {'0': 0,'1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
        
        num_1 = 0
        num_2 = 0
        
        for i in range(len(num1)-1, -1, -1):
            digit = digit_map[num1[i]]
            num_1 += digit*(10**(len(num1) - i - 1))
            
        for i in range(len(num2)-1, -1, -1):
            digit = digit_map[num2[i]]
            num_2 += digit*(10**(len(num2) - i - 1))
        
        print(num_1, num_2)
        
        mult = num_1 * num_2
        return str(mult)