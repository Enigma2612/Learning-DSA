from tree_utils import *

def bfs(root):
    ans = []
    queue = [root]
    l = 0
    while l < len(queue):
        el = queue[l]
        ans.append(el.val)
        if el.left: queue.append(el.left)
        if el.right: queue.append(el.right)
        l += 1
    return ans

tree_1 = make_tree([1,2,3,4,5,10])

print(bfs(tree_1))