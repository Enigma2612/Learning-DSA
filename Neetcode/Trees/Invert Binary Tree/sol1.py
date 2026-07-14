from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return
        stack = [root]
        while stack:
            el = stack.pop()
            if el.right: stack.append(el.right)
            if el.left: stack.append(el.left)
        
            el.left, el.right = el.right, el.left
        return root