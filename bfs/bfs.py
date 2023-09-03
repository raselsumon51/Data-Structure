from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque()
    
    visited.add(start)
    queue.append(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("Breadth-First Traversal (starting from vertex 2):")
bfs(graph, 2)
