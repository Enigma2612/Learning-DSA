class Solution:
    def findMin(self, nums: list[int]) -> int:
        min_el = nums[0]

        l,r = 0, len(nums)-1
        
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] < min_el:
                min_el = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        
        return min_el
    
#my first solution
#works pretty well
