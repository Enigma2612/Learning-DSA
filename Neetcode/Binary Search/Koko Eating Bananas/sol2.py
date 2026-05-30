class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l,r = 1, max(piles)

        ans = r

        while l <= r:
            mid = l + (r-l)//2
            counter = 0
            for i in piles:
                counter += (i//mid + int(bool(i%mid)))
                if counter > h:
                    break
        
            if counter <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
        return ans

#The simplest approach turned out to be the best one