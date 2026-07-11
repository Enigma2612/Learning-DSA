class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

def make_tree(lis):
    lis2 = [Node() for _ in range(len(lis))]
    
    for i in range(len(lis)-1, -1, -1):
        lis2[i].val = lis[i]
        if 2*i + 1 < len(lis):
            lis2[i].left = lis2[2*i+1]
        if 2*i + 2 < len(lis):
            lis2[i].right = lis2[2*i+2]
    return lis2[0]
