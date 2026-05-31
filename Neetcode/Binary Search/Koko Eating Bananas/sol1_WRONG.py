class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        piles.sort()
        biggers = {}

        min_el = piles[0]
        max_el = piles[-1]

        counter = 0
        p = len(piles)-1
        
        for i in range(len(piles)-1, -1, -1):
            while piles[i] < piles[p] and p >= 0:
                counter += 1
                p -= 1
            else:
                biggers[piles[p]] = counter
    
        lis = [i for i in range(1, min_el)] + sorted(set(piles))

        l,r = 0, len(lis) - 1

        ans = max_el

        while l <= r:
            mid = l + (r-l)//2
            if lis[mid] < min_el:
                excess = len(piles)
            else:
                excess = biggers[lis[mid]]
            
            if excess < (h - len(piles)):
                ans = min(piles[mid], max_el)
                r = mid - 1
            else:
                l = mid + 1
        
        return ans

            


            
#DOES NOT WORK
#I made a very interesting mistake, so thought I'd include it
#Intent: Trying to save on time complexity using extra space
#Mistake here: The computations for each specific case also depend on the case
#so space doesn't help as much

#Detailed mistake: I tried to store how many bigger towers exist before each tower in the sorted list
#But the problem is, just knowing a tower is bigger doesn't tell me how many moves it will take to consume it