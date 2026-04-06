class Solution:
    def hasDuplicate(self, nums) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False

#Time: O(N)
#Space: O(N)