class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        for i in range(1,len(intervals)):
            if merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])     # No change as intervals are not overlapping
            else:
                merged[-1][1] = max(merged[-1][1],intervals[i][1]) # Interval overalps hence needs to be changed
        return merged