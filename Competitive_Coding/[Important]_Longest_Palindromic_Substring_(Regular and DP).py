# Problem URL: https://leetcode.com/problems/longest-palindromic-substring/

# Dynamic Programming Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 2D Table for Memoization 
        dp = [[False]*len(s) for i in range(len(s))]
        length = 0
        result = ''

        for end in range(len(s)):
            for start in range(end+1):
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = (s[start] == s[end])
                else:
                    dp[start][end] = (s[start] == s[end] and dp[start+1][end-1])

                if (dp[start][end] and end-start+1 > length):
                    length = end-start+1
                    result = s[start:end+1]

        return result


# Regular Solution
from itertools import combinations

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # Function to Check if Substring is Palindrome or not
        def isPalinDrome(substring: str) -> int:
            if len(substring) == 1:
                return 1
            else:
                begin = 0
                end = len(substring)-1
                while (begin<end):
                    if (substring[begin] == substring[end]):
                        begin += 1
                        end -= 1
                    else:
                        return 0
                return 1
        
        # Create Substrings and Sort them in reverse order of length
        #all_substrings = [s[x:y] for x,y in combinations(range(len(s)+1), r = 2)]
        #all_substrings.sort(key = lambda x: len(x), reverse = True)
        
        #for subs in all_substrings:
        #    if isPalinDrome(subs) == 1:
        #        return subs
        
        for length in range(len(s),-1,-1):
            substrings = []
            for begin in range(len(s)-length + 1):
                end = begin + length - 1
                substrings.append(s[begin:end+1])
            for subs in substrings:
                if isPalinDrome(subs) == 1:
                    return subs