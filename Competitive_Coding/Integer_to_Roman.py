# Problem URL: https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        
        # Handling subtraction cases
        corners = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
        if num in list(corners.keys()):
            return corners[num]
        else:
            romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC',
                      50: 'L',  40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
            required = {}
            idx = 0
            while (num > 0):
                i = list(romans.keys())[idx]
                contains = num//i
                if contains>0:
                    required[i] = contains
                    num -= contains*i
                idx += 1
            
            roman_number = ''
            for i in list(required.keys()):
                roman_number += romans[i]*required[i]
            
            return roman_number