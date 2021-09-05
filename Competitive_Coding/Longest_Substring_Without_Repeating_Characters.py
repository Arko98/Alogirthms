from itertools import combinations
from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Using Hashmap
        left = 0
        right = 0
        count = 0
        hash_map = {}
        
        while (right <= len(s)-1):
            if s[right] in hash_map and hash_map[s[right]] >= left:
                count = max(count, right - left)
                left = hash_map[s[right]]+1
            hash_map[s[right]] = right
            right += 1
        count = max(count, right - left)
        return count
    
        '''
        # Using Itertools and built-in Functions (986/987 Test Case Passed)       
        if s == "":
            return 0
        else:
            out_len = 0
            all_substrings = [s[x:y] for x,y in combinations(range(len(s)+1),r=2)]

            #all_substrings = []
            #for length in range(1, len(s)+1):
            #    for i in range(len(s) - length + 1):
            #        j = i + length - 1
            #        all_substrings.append(s[i:j+1])
            
            all_substrings.sort(key = lambda x: len(x), reverse = True)
            for i in range(len(all_substrings)):
                flag = 0
                count = Counter(all_substrings[i])
                count_vals = list(count.values())
                for j in count_vals:
                    if j > 1 :
                        flag = 1
                        break
                if flag == 0:
                    out_len = len(all_substrings[i])
                    return out_len
        '''