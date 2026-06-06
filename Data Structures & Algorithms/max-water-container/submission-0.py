class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        l = 0
        r = n - 1
        while l < r:
            temp_area = min(heights[l], heights[r]) * (r-l)
            max_area = max(temp_area, max_area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_area