Problem URL: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for i in range(len(nums)-2):
            a = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                if a+b+c == 0:
                    if [a,b,c] not in solution:
                        solution.append([a,b,c])
                    start += 1
                    end -= 1
                elif a+b+c > 0:
                    end -= 1
                else:
                    start += 1
        return solution 