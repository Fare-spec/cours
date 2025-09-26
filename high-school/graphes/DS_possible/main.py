graphe = {
    "node1": ["node2", "node4"],
    "node2": ["node2", "node3", "node6"],
    "node3": ["node5"],
    "node5": ["node5", "node6"],
    "node4": ["node1", "node5"],
    "node6": [],
}
print(graphe["node1"])


def bfs(graphe, start_node):
    queue = [start_node]

    visited = set()
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graphe[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


bfs(graphe, "node1")
