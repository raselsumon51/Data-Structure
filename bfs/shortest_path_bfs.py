from collections import deque

def bfs_shortest_path(graph, start, end):
    queue = deque()
    queue.append((start, [start]))
    
    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == end:
            return path

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor])) 

    return None

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

start_node = 1
end_node = 6

shortest_path = bfs_shortest_path(graph, start_node, end_node)
if shortest_path:
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
else:
    print(f"No path found from {start_node} to {end_node}")
