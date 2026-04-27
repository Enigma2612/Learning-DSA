class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        b,s = 0,1
        if len(prices) < 2:
            return 0
        curr = prices[s] - prices[b]

        for ind, i in enumerate(prices):
            if i - prices[b] > curr:
                s = max(s,ind)
                curr = prices[s] - prices[b]
            elif i < prices[b]:
                b = ind
    
        return max(curr, 0)

            
#similar to kadane's algorithm