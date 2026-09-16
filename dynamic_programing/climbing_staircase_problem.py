"""
Dynamic programming works when two key conditions are present in a problem.

1. Overlapping Subproblems: The same smaller problems appear multiple times when solving
the larger problem. Instead of recalculating these subproblems repeatedly, we store their solutions.

2. Optimal Substructure: The optimal solution to the problem contains optimal solutions to its
subproblems. This means we can build up the best solution by combining the best solutions to
smaller parts.

Dynamic programming is effective when:

    1. The problem can be broken down into overlapping subproblems.

    2. The problem exhibits optimal substructure.

    3. A naive recursive solution would involve repeated calculations.

    4. You need to optimize for time complexity at the cost of space complexity.

    Common dynamic programming patterns include optimization problems (finding minimum/maximum values),
    counting problems (number of ways to achieve something), and decision problems that can be
    broken down into smaller decisions.
"""


def climb_stairs_recursive(n):
    """Recursive approach"""
    print(f"Climbing stairs {n}")
    if n <= 2:
        return n  # Base cases: 1 way for 1 step, 2 ways for 2 steps
    # To reach step n, we can come from step (n-1) or step (n-2)
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


def climbing_staircase_memoized(n, memo={}):
    """Memoization (Top-Down Approach)
    Time complexity: Reduced from O(2^n) to O(n) since we make only n unique calculations
    Space complexity: O(n) for the memo storage and call stack
    """
    # Check if we've already calculated this value
    if n in memo:
        return memo[n]  # Return cached result - O(1) lookup!

    print(f"Climbing stairs {n}")
    # Base cases
    if n <= 2:
        return n

    # Calculate once and store in memo for future use
    memo[n] = climbing_staircase_memoized(n - 1, memo) + climbing_staircase_memoized(
        n - 2, memo
    )
    return memo[n]


def climb_stairs_tabulation(n):
    """Tabulation (Bottom-Up Approach)
    Time complexity: O(n) instead of O(2^n).
    Space complexity: O(n) for the array, or O(1) with optimization.
    """
    if n <= 2:
        return n

    # Create array to store results for all steps from 0 to n
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way to reach step 1
    dp[2] = 2  # 2 ways to reach step 2

    # Build up the solution iteratively
    for i in range(3, n + 1):
        # Ways to reach step i = ways to reach (i-1) + ways to reach (i-2)
        print(f"Climbing stairs {i}")
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def climb_stairs_optimized(n):
    if n <= 2:
        return n

    prev2, prev1 = 1, 2  # Only store last two values
    for i in range(3, n + 1):
        print(f"Climbing stairs {i}")
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    return prev1


if __name__ == "__main__":
    # print(climb_stairs_recursive(50))
    # print(climbing_staircase_memoized(50))
    # print(climb_stairs_tabulation(50))
    print(climb_stairs_optimized(50))
