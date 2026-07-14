#Graph structure: Edge-dictionary {node: [*neighbors]}

def rec_dfs(graph):
    seen = set()
    ans = []
    def helper(node):
        if node in seen:
            return
        seen.add(node)
        ans.append(node)
        for new in graph.get(node, []):
            helper(new)
    helper(list(graph)[0])
    return ans


def it_dfs(graph):
    stack = []
    seen = set()
    ans = []
    stack.append(list(graph)[0])
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        ans.append(node)
        stack.extend(graph.get(node, [])) 

    return ans

graph_1 = {1: [2, 3], 2: [4, 5, 1], 3: [10], 10: [1]}

print(rec_dfs(graph_1))
print(it_dfs(graph_1))