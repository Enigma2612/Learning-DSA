class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        freq = {}
        res = []

        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        zeros = freq.get(0,0)

        if zeros > 1:
            return [0]*len(nums)
    
        p = 1
        for i in freq:
            if not i: continue
            p *= i ** freq[i]
    
        for i in nums:
            if zeros:
                if i:
                    res.append(0)
                else:
                    res.append(p)
            else:
                res.append(p//i)

        return res