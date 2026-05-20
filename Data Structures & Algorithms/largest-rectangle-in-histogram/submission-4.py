class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        start = 0
        max_area = 0
        stck = []
        for i, height in enumerate(heights):
            start = i
            while stck and height <= stck[-1][0]:
                h,j =  stck.pop()
                w = i-j
                area = h * w
                max_area = max(max_area, area)
                start = j
            stck.append((height, start))
        
        while stck:
            h , j = stck.pop()
            w = n - j
            area = h * w
            max_area = max(max_area, area)
        
        return max_area