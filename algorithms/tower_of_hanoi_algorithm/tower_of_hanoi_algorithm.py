def hanoi_solver(n):
    """
    Solves the Tower of Hanoi puzzle and returns a string of all moves.

    Args:
        n (int): Number of disks

    Returns:
        str: String with starting arrangement and all moves, each on a new line.
             Rods are represented as lists separated by spaces.
    """

    # Initialize the three rods
    source = list(range(n, 0, -1))  # [n, n-1, ..., 2, 1]
    auxiliary = []
    destination = []

    # Store all states
    states = [f"{source} {auxiliary} {destination}"]

    def solve(num_disks, src, dest, aux):
        """Recursive helper to solve Tower of Hanoi."""
        if num_disks == 1:
            # Move disk from source to destination
            disk = src.pop()
            dest.append(disk)
            states.append(f"{source} {auxiliary} {destination}")
            return

        # Move n-1 disks from source to auxiliary using destination
        solve(num_disks - 1, src, aux, dest)

        # Move the largest disk from source to destination
        disk = src.pop()
        dest.append(disk)
        states.append(f"{source} {auxiliary} {destination}")

        # Move n-1 disks from auxiliary to destination using source
        solve(num_disks - 1, aux, dest, src)

    # Solve the puzzle
    solve(n, source, destination, auxiliary)

    # Return all states as a single string, one per line
    return "\n".join(states)


# Test it
if __name__ == "__main__":
    print(hanoi_solver(3))
