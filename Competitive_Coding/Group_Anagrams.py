# Problem URL: Group Anagrams

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for d in strs:
            data[tuple(sorted(d))].append(d)
            
        return data.values()