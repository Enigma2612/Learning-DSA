class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1

        num_1, num_2 = 0, 0

        for i in nums:
            if (target-i) == i:
                if freq.get(target-i) > 1:
                    num_1 = i
                    num_2 = target-i
                    break
            else:
                if freq.get(target-i, 0):
                    num_1 = i
                    num_2 = target-i
                    break

        p1,p2 = -1,-1
        for i in range(len(nums)):
            if nums[i] in [num_1,num_2]:
                if p1 < 0:
                    p1 = i
                else:
                    p2 = i
                    break
        
        return [p1,p2]
            
