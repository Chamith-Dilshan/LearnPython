def dfs_n_queens(n):
    if not isinstance(n, int):
        return []
    # Edge case: invalid board size
    if n < 1:
        return []

    solutions = []
    current_solution = []

    def is_valid(row, col):
        """Check if placing a queen at (row, col) is safe."""
        # Check each previously placed queen
        for prev_row in range(row):
            prev_col = current_solution[prev_row]

            # Check column conflict
            if prev_col == col:
                return False

            # Check diagonal conflict
            # Two positions are on the same diagonal if the absolute difference
            # between their rows equals the absolute difference between their columns
            if abs(prev_row - row) == abs(prev_col - col):
                return False

        return True

    def dfs(row):
        """Recursively place queens using DFS."""
        # Base case: all queens placed successfully
        if row == n:
            solutions.append(current_solution[:])  # Add a copy of the solution
            return

        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_valid(row, col):
                # Place queen
                current_solution.append(col)

                # Explore next row
                dfs(row + 1)

                # Backtrack: remove queen and try next column
                current_solution.pop()

    dfs(0)
    return solutions


if __name__ == "__main__":
    print(dfs_n_queens(4))
