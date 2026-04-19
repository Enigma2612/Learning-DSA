class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        triplets = set()

        for ind,i in enumerate(nums):
            target = -i
            l,r = ind+1, len(nums)-1
            while l<r:
                curr = nums[l] + nums[r]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    triplets.add((i,nums[l],nums[r]))
                    l += 1
        
        return [list(i) for i in triplets]

        