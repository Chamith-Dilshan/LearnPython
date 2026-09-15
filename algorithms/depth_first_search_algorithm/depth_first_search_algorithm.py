def dfs(adjacency_matrix, start_node):
    # Initialize a set to track visited nodes
    visited = set()

    # Initialize a stack with the starting node
    stack = [start_node]

    # Continue while there are nodes to explore
    while stack:
        # Pop the last node added to the stack (LIFO)
        node = stack.pop()

        # If we haven't visited this node yet
        if node not in visited:
            # Mark it as visited
            visited.add(node)

            # Iterate through all neighbors of the current node
            for neighbor in range(len(adjacency_matrix[node])):
                # If there's an edge to this neighbor and it hasn't been visited
                if adjacency_matrix[node][neighbor] == 1 and neighbor not in visited:
                    # Add the neighbor to the stack for exploration
                    stack.append(neighbor)

    # Return the list of reachable nodes (sorted for consistency)
    return sorted(list(visited))


if __name__ == "__main__":
    adjacency_matrix = [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]
    print(dfs(adjacency_matrix, 0))
