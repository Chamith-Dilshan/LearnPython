def adjacency_list_to_matrix(adj_list):
    # Get the number of nodes (size of the matrix)
    n = len(adj_list)

    # Create an n × n matrix initialized with zeros
    matrix = [[0] * n for _ in range(n)]

    # Populate the matrix based on the adjacency list
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1

    # Print each row of the matrix
    for row in matrix:
        print(row)

    # Return the adjacency matrix
    return matrix


if __name__ == "__main__":
    adjacency_list = {0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}
    print(adjacency_list_to_matrix(adjacency_list))
