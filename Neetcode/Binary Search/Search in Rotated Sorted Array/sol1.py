class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[l]: #sorted left
                if nums[l] > target or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else: #sorted right
                if nums[r] < target or nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

        
        return -1

#Very interesting approach
#I was on the right track, but took some help to figure it out
#Not fully my solution