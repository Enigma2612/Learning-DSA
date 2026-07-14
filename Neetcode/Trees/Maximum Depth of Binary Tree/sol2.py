from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack = [[root, 1]]
        
        ans = 1
        while stack:
            el, lvl = stack.pop()
            ans = max(ans, lvl)
            if el.left:
                stack.append([el.left, lvl+1])
            if el.right:
                stack.append([el.right, lvl+1])

        return ans

