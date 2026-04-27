class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opps = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in ['(', '{', '[']:
                stack.append(i)
            elif stack == []:
                return False
            elif stack[-1] == opps[i]:
                stack.pop()
            else:
                return False
        
        if not stack:
            return True
        else:
            return False
        