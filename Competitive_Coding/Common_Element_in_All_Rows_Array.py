def common(arr,row,col):
    # Initialize hash_map with first row elements
    hash_map = {i:1 for i in arr[0]} 
    for row_idx in range(1,row):
        for col_idx in range(col):
            if arr[row_idx][col_idx] not in list(hash_map.keys()):
                continue
            elif arr[row_idx][col_idx] in list(hash_map.keys()) and hash_map[arr[row_idx][col_idx]] < row_idx + 1:
                hash_map[arr[row_idx][col_idx]] += 1

    out_list = []            
    for key in hash_map:
        if hash_map[key] == row:
            out_list.append(key)
    return out_list
        

# Driver Code
mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
print(common(mat,4,5))