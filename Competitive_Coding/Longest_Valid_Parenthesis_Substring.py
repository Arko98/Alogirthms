# Problem URL: https://leetcode.com/problems/longest-valid-parentheses

# FastStack Solution
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
  
        stack=[]
        max_len=0
        temp_len=0
        for char in s:
            if char=='(':
                stack.append(temp_len)
                temp_len=0
            elif char==')':
                if stack:
                    temp_len+=stack.pop()+2
                    max_len=max(temp_len,max_len)
                else:
                    temp_len=0
             
        return max_len
        

# Simple Stack Solution
from itertools import combinations
class Solution:
    def isValid(self, s: str) -> bool:
        # Corner Case Handling
        if s == '':
            return 0
        
        # Base Case Handling
        top = -1
        stack = [0 for i in range(len(s))]
        for i in s:
            if (i == '(' or i == '{' or i == '['):
                top += 1
                stack[top] = i
            elif (i == ')' or i == '}' or i == ']'):
                if ((i == ')' and stack[top] == '(') or (i == '}' and stack[top] == '{') or (i == ']' and stack[top] == '[')):
                    top -= 1
                else:
                    return 0
        if (top == -1):
            return 1
    
    def longestValidParentheses(self, s: str) -> int:
        #longestValidString = 0
        max_length = 0
        parenthesis_substrings = [s[x:y] for x,y in combinations(range(len(s)+1),r=2)]
        
        for string in parenthesis_substrings:
            if self.isValid(string) == True:
                if (len(string) > max_length):
                    max_length = len(string)
                    #longestValidString = string
        
        return max_length