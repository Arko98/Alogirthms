# Problem Statement: 

# Solution
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if needle == "":
            return 0
        
        if haystack == "":
            return -1
        
        
        found = 0
        found_idx = 0
        needle_length = len(needle)
        for i in range(len(haystack) - len(needle) + 1):
            if needle[0] != haystack[i]:
                continue
            else:
                needle_idx = 1
                i += 1
                while (needle_idx < needle_length and needle[needle_idx] == haystack[i]):
                    i += 1
                    needle_idx += 1
                if needle_idx == needle_length:
                    found_idx = i - needle_length
                    found = 1
                    break
        
        if found == 1:
            return found_idx
        
        elif found == 0:
            return -1


# Inbuilt function
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle)==0):
            return 0
        elif (len(haystack)==0):
            return -1
        else:
            return haystack.find(needle, 0, len(haystack))