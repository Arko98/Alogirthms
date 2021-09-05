# Problem URL: https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(i) for i in strs]
        min_length = min(lengths)
        for length_val in range(min_length,-1,-1):
            if length_val > 0:
                prefixes = [i[:length_val] for i in strs]
                flag = 0
                for prefs in prefixes[1:]:
                    if (prefs != prefixes[0]):
                        flag = 1
                        break
                if flag == 0:
                    return prefixes[0]
            else:
                return ''