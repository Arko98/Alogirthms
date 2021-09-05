# Problem URL: https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        size = len(height)
        left, right = 0, size - 1
        max_width = size - 1
        area = 0
        
        for width in range(max_width,0,-1):
            if (height[left]<height[right]):
                area = max(area, (width * height[left]))
                left += 1
            else:
                area = max(area,(width * height[right]))
                right -= 1
        
        return area    