# Solution with Binary Search

class Solution:
    def binary_search(self,arr,target,begin,end):
        while (begin <= end):
            mid = (begin + end)//2
            if target == arr[mid]:
                return True
            elif target > arr[mid]:
                return self.binary_search(arr,target,mid + 1,end)
            else:
                return self.binary_search(arr,target,begin,mid - 1)
        return False
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        out_list = []
        for i in A:
            if self.binary_search(A,i,0,n1) == self.binary_search(B,i,0,n2) == self.binary_search(C,i,0,n3) == True:
                out_list.append(i)
        final_list = list(set(out_list))
        final_list.sort()
        return final_list

# Solution with Hash-Map

class Solution:
    def commonElements (self, A, B, C, n1, n2, n3):
        # your code here
        hash_map_1 = {i:0 for i in range(min(A),max(A)+1)}
        hash_map_2 = {i:0 for i in range(min(B),max(B)+1)}
        hash_map_3 = {i:0 for i in range(min(C),max(C)+1)}
        for i in A:
            hash_map_1[i] += 1
        for i in B:
            hash_map_2[i] += 1
        for i in C:
            hash_map_3[i] += 1
            
        out_list = []
        for key in hash_map_1:
            try:
                if (hash_map_1[key] > 0) and (hash_map_2[key] > 0) and (hash_map_3[key] > 0):
                    out_list.append(key)
            except KeyError:
                pass
        return sorted(out_list)