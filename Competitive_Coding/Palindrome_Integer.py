# Problem URL: https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = [i for i in str(x)]
        s_rev = s[::-1]
        if  s == s_rev :
            return True
        else:
            return False