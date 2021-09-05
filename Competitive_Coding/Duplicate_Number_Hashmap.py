class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        keys = list(set(nums))
        hash_map = {i:0 for i in keys}
        
        for i in nums:
            hash_map[i] += 1
        
        for i in keys:
            if hash_map[i] > 1:
                return i