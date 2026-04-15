class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        freq_map = {}
        count = 0
        for i in nums:
            freq_map[i] = freq_map.get(i,0)+1
        
        for i in nums:
            if (i-1) not in freq_map:
                k = 1
                while i+k in freq_map:
                    k += 1
                count = max(count, k)
        return count
            
