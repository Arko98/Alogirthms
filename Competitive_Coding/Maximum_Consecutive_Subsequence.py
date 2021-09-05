def findLongestConseqSubseq(arr, N):
        #code here
        hash_map = {i:0 for i in range(max(arr)+1)}
        for i in range(len(arr)):
            hash_map[arr[i]] += 1
        max_count = 0
        count = 0
        for i in hash_map:
            if i+1 in hash_map and (hash_map[i]>0 and hash_map[i+1]>0):
                count += 1
                if count > max_count:
                    max_count = count
            elif hash_map[i]==0 or (i+1 in hash_map and (hash_map[i]>0 and hash_map[i+1]==0)):
                count = 0
        return max_count+1