# Problem URL: https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            if merged[-1][1] < intervals[i][0]: merged.append(intervals[i])  # No Merge
            else: merged[-1][1] = max(merged[-1][1], intervals[i][1])        # change entry accordingly
        
        return merged