class Solution:
    def trap(self, heights: list[int]) -> int:
        max_height = max(heights)
        height_freqs = [0]*(max_height+1)
        for i in heights:
            height_freqs[i] += 1

        cum_height_freqs = [0]*(max_height+1)
        cum_height_freqs[max_height] = height_freqs[max_height]
        for i in range(max_height-1, -1, -1):
            cum_height_freqs[i] = cum_height_freqs[i+1] + height_freqs[i]
        
        water = 0
        level = 1
        l,r = 0,len(heights)-1

        while l<r and level < max_height+1:
            while heights[l] < level and l<r:
                l += 1
            while heights[r] < level and l<r:
                r -= 1
            
            water += (r-l+1 - cum_height_freqs[level])
            level += 1
    
        return water

#my old solution
#I don't remember how it works xD
#gotta go through it again