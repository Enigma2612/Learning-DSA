class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = {}
        freq_lis = [[] for _ in range(len(nums)+1)]

        for i in nums: 
            counter[i] = counter.get(i, 0) + 1
            
        for n,c in counter.items():
            freq_lis[c].append(n)
    
        res = []
        
        for j in range(len(nums), 0, -1):
            for num in freq_lis[j]:
                res.append(num)
                if len(res) == k:
                    return res
        
