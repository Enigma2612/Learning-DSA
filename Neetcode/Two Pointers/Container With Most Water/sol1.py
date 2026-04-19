class Solution:
    def maxArea(self, heights: list[int]) -> int:
        area = 0
        l,r = 0, len(heights)-1
        while l<r:
            area = max(area, (r-l)*min(heights[l], heights[r]))

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return area
    
#beautiful question