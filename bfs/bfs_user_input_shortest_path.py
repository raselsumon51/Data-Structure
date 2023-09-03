from collections import defaultdict, deque

def bfs_shortest_path(graph, start, end):
    visited = set()
    queue = deque()
    
    visited.add(start)
    queue.append((start, [start]))  # Tuple containing vertex and path
    
    while queue:
        vertex, path = queue.popleft()
        
        if vertex == end:
            return path  # Return the shortest path if the destination is reached
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

edges_input = input("Enter edges (format: u1 v1, u2 v2, ...): ")
start_vertex, end_vertex = map(int, input("Enter start and end vertex (format: start end): ").split())

graph = defaultdict(list)

edges = edges_input.split(", ")
for edge in edges:
    u, v = map(int, edge.split())
    graph[u].append(v)

shortest_path = bfs_shortest_path(graph, start_vertex, end_vertex)

if shortest_path:
    print(f"Shortest path from {start_vertex} to {end_vertex}: {shortest_path}")
else:
    print(f"No path from {start_vertex} to {end_vertex} found.")


# 0 1, 0 3, 1 2, 3 4, 3 7, 4 5, 4 6, 4 7, 5 6 , 6 7
# 0 7


# 0 1, 0 3, 1 2, 2 0, 2 3, 3 3
# 2 3

