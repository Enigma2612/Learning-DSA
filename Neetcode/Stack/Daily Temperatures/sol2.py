class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = []
        stack = []      #storing only indices

        for i in range(len(temperatures)-1, -1, -1):
            val = temperatures[i]
            
            while stack and temperatures[stack[-1]] <= val:
                stack.pop()
                
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1] - i)
            
            stack.append(i)

        return ans[::-1]
    
#Similar to previous solution, but less memory usage (Same order, but smaller mult)