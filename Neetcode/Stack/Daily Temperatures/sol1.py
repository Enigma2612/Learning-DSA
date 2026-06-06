class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        ans = []
        stack = []      #storing (index, value)

        for i in range(len(temperatures)-1, -1, -1):
            val = temperatures[i]
            
            while stack and stack[-1][1] <= val:
                stack.pop()
                
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1][0] - i)
            
            stack.append((i, val))

        return ans[::-1]
    
