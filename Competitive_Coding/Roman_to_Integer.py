# Problem URL: https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        corners = {'IV': 4 , 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        romans = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90,
                  'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
    
        # Handling Corner Cases
        if s in list(corners.keys()):
            return corners[s]

        # Regular Case
        else:            
            start = 0
            number = 0
            while (start<len(s)):
                #if (start+2 < len(s) and  s[start:start+2] in corners):
                #    number += corners[s[start:start+2]]
                #    start += 2
                if (start+2 <= len(s) and s[start:start+2] in romans):
                    print(start, s[start:start+2])
                    number += romans[s[start:start+2]]
                    start += 2
                elif (s[start] in romans):
                    print(start, s[start])
                    number += romans[s[start:start+1]]
                    start += 1

            return number
        