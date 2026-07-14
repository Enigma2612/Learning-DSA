#Graph structure: Edge-dictionary {node: [*neighbors]}

def bfs(graph):
    queue = []
    seen = set()
    ans = []
    l = 0
    queue.append(list(graph)[0])
    while l < len(queue):
        if queue[l] in seen:
            l += 1
            continue
        seen.add(queue[l])
        queue.extend(graph.get(queue[l], []))
        ans.append(queue[l])
        l += 1
    return ans

graph_1 = {1: [2, 3], 2: [4, 5, 1], 3: [10], 10: [1]}

print(bfs(graph_1))
