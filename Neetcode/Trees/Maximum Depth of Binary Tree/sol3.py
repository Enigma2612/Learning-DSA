from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = [root]
        l = 0

        level = 0

        while l < len(queue):
            x = l
            for i in range(x, len(queue)):
                l += 1
                if queue[i].left: queue.append(queue[i].left)
                if queue[i].right: queue.append(queue[i].right)

            level += 1
        
        return level
