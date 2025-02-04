# Chatgpt code

import heapq

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    distances[source] = 0
    
    previous = {node: None for node in graph}
    
    queue = [(0, source)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))
    
    return distances, previous

def reconstruct_path(previous, start, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path

if __name__ == '__main__':
    graph = {
        "R1": [("R2", 1)],
        "R2": [("R3", 1), ("R5", 10)],
        "R3": [("R4", 1), ("R5", 1)],
        "R5": [("R4", 10)],
        "R4": []
    }
    
    source = "R1"
    destination = "R4"
    
    distances, previous = dijkstra(graph, source)
    
    print("Shortest distances from", source, ":", distances)
    
    path = reconstruct_path(previous, source, destination)
    print("Shortest path from", source, "to", destination, ":", path)

