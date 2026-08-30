# Square root bisection is a numerical algorithm that uses the bisection method to find
# the square root of a number. It works by repeatedly narrowing down an interval that
# contains the square root until you reach the desired precision.
#
# The basic idea treats the problem as finding where the function f(x) = x² - n
# equals zero (where n is the number you want the square root of).
# The bisection method then:
#
# Starts with an interval [low, high] that you know contains the square root
# Calculates the midpoint
# Tests whether the midpoint's square is too high or too low
# Narrows the interval based on that test
# Repeats until the interval is small enough


def square_root_bisection(
        number: float, tolerance: float = 0.01, maxiterations: int = 10
):
    """
    Find the square root of n using the bisection method.

    Args:
        number: The number to find the square root of
        tolerance: How close to the actual value we need to be
        maxiterations: The maximum number of iterations

    Returns:
        The approximate square root of n, or None if it fails
    """
    if number < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )
    if number == 0:
        print("The square root of 0 is 0")
        return 0
    if number == 1:
        print("The square root of 1 is 1")
        return 1

    # Set initial interval based on the number
    if number > 1:
        low = 0
        high = number
    else:  # 0 < number < 1
        low = 0
        high = 1

    iteration = 0

    # Keep bisecting until tolerance is met or max iterations reached
    while high - low > tolerance and iteration < maxiterations:
        mid = (low + high) / 2
        square = mid ** 2

        if square < number:
            low = mid
        else:
            high = mid
        iteration += 1

    # Return result if converged
    if high - low <= tolerance:
        result = (low + high) / 2
        print(f"The square root of {number} is approximately {result}")
        return result
    else:
        print(f"Failed to converge within {maxiterations} iterations")
        return None


def main():
    print(square_root_bisection(0.001, 1e-7, 50))  # Should print ~0.0316...
    print(square_root_bisection(16, 0.01, 50))  # Should print ~4.0
    print(square_root_bisection(2, 0.01, 50))  # Should print ~1.414...
    print(square_root_bisection(0.25, 1e-7, 50))


if __name__ == "__main__":
    main()
