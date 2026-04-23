class Solution:
    def trap(self, height: list[int]) -> int:
        pre_max_heights = [0]
        post_max_heights = [0]

        water = 0

        for i in range(len(height)-1):
            pre_max_heights.append(max(height[i], pre_max_heights[-1]))
        
        for i in range(len(height)-1, 0, -1):
            post_max_heights.append(max(height[i], post_max_heights[-1]))
        
        post_max_heights = post_max_heights[::-1]

        for i in range(len(height)):
            water += max(min(post_max_heights[i], pre_max_heights[i]) - height[i], 0)

        return water
    

#my most recent attempt
#doesn't use two pointer xD