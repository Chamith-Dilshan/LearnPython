def quick_sort(array):
    """
    Sort a list of integers using the quicksort algorithm.
    Does NOT modify the original list.

    Args:
        array: A list of integers to sort

    Returns:
        A new sorted list in ascending order
    """
    # Base case: arrays with 0 or 1 elements are already sorted
    if len(array) <= 1:
        return array

    # Choose pivot (using first element)
    pivot_value = array[0]

    # Partition into three sublists (creates new lists, doesn't modify original)
    less_values = []
    equal_values = []
    greater_values = []

    for value in array:
        if value < pivot_value:
            less_values.append(value)
        elif value > pivot_value:
            greater_values.append(value)
        else:
            equal_values.append(value)

    # Recursively sort and concatenate
    return quick_sort(less_values) + equal_values + quick_sort(greater_values)


# Test cases from your requirements
def test_quick_sort():
    # Test 1: Original list should not be modified
    original = [20, 3, 14, 1, 5]
    original_copy = original.copy()
    result = quick_sort(original)
    assert original == original_copy, "Original list was modified!"
    assert result == [1, 3, 5, 14, 20]
    print("✓ Test 1 passed: [20, 3, 14, 1, 5] → [1, 3, 5, 14, 20]")

    # Test 2
    original = [83, 4, 24, 2]
    original_copy = original.copy()
    result = quick_sort(original)
    assert original == original_copy, "Original list was modified!"
    assert result == [2, 4, 24, 83]
    print("✓ Test 2 passed: [83, 4, 24, 2] → [2, 4, 24, 83]")

    # Test 3
    original = [4, 42, 16, 23, 15, 8]
    original_copy = original.copy()
    result = quick_sort(original)
    assert original == original_copy, "Original list was modified!"
    assert result == [4, 8, 15, 16, 23, 42]
    print("✓ Test 3 passed: [4, 42, 16, 23, 15, 8] → [4, 8, 15, 16, 23, 42]")

    # Test 4
    original = [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]
    original_copy = original.copy()
    result = quick_sort(original)
    assert original == original_copy, "Original list was modified!"
    assert result == [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]
    print(
        "✓ Test 4 passed: [87, 11, 23, 18, 18, 23, 11, 56, 87, 56] → [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]"
    )

    # Additional edge cases
    assert quick_sort([]) == []
    print("✓ Test 5 passed: Empty list")

    assert quick_sort([1]) == [1]
    print("✓ Test 6 passed: Single element")

    assert quick_sort([5, 5, 5]) == [5, 5, 5]
    print("✓ Test 7 passed: All identical elements")

    assert quick_sort([3, 1, 2]) == [1, 2, 3]
    print("✓ Test 8 passed: Small unsorted list")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_quick_sort()
