def majorityElement(nums: List[int]) -> List[int]:
        hash_map = {i:0 for i in range(min(nums),max(nums)+1)}
        for i in range(len(nums)):
            hash_map[nums[i]] += 1
        out_list = []
        for i in hash_map:
            if hash_map[i] > math.floor(len(nums)/3):
                out_list.append(i)
        return out_list