from tree_utils import *

#iterative dfs
def it_dfs(root):
    stack = [root]
    ans = []
    while stack:
        el = stack.pop()
        if el.right and el.right.val:
            stack.append(el.right)
        if el.left and el.left.val:
            stack.append(el.left)
        ans.append(el.val)
    return ans

#recursive dfs
def rec_dfs(root):
    ans = []
    def dfs(root):
        if root and root.val:
            ans.append(root.val)
            dfs(root.left)
            dfs(root.right)
    dfs(root)
    return ans

tree_1 = make_tree([1,2,3,4,5,10])
print(it_dfs(tree_1))
print(rec_dfs(tree_1))

