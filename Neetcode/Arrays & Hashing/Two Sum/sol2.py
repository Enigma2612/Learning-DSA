class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i,n in enumerate(nums):
            if (d:=(target - n)) in dic:
                return [dic[d],i]
            else:
                dic[n] = i
            
#sol on neetcode, not mine
#very interesting, and easy
