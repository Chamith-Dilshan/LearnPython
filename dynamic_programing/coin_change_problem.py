"""
Determine the minimum number of coins required to achieve a specific amount.

This function utilizes dynamic programming to compute the minimum number of
coins needed to make up the specified amount using the given list of coin
denominations. If it is not possible to achieve the target amount using the
provided denominations, the function returns -1.

Parameters:
amount: int
    The target amount for which the minimum number of coins is calculated.
coins: list of int
    The list of available coin denominations.

Returns:
int
    The minimum number of coins required to achieve the target amount, or -1
    if it is not possible.
"""


def min_coins(amount, coins):
    """Find minimum number of coins needed to make the given amount"""
    # Initialize dp array with "infinity" - represents impossible to make
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # For each amount from 1 to target amount
    for i in range(1, amount + 1):
        # Try each coin denomination
        for coin in coins:
            if coin <= i:  # Can only use coin if it doesn't exceed current amount
                # Update minimum: current minimum vs (coins for remaining amount + 1)
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return result if possible, -1 if impossible
    return dp[amount] if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    print(min_coins(10, [1, 2, 5]))
