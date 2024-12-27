from collections import deque

def bfs(graph, start):
    """
    Perform BFS on a graph and return the order of traversal.
    
    Parameters:
    graph (dict): A dictionary representing the adjacency list of the graph.
    start (any): The starting node for BFS.
    
    Returns:
    list: A list of nodes in the order they are visited.
    """
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Use a queue to manage the BFS
    traversal_order = []  # To store the BFS traversal order

    while queue:
        current = queue.popleft()  # Get the next node in the queue
        if current not in visited:
            visited.add(current)  # Mark as visited
            traversal_order.append(current)  # Add to the result
            # Add all unvisited neighbors to the queue
            queue.extend(neighbor for neighbor in graph[current] if neighbor not in visited)
    
    return traversal_order

# Example usage
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    start_node = 'A'
    print("BFS Traversal:", bfs(graph, start_node))
