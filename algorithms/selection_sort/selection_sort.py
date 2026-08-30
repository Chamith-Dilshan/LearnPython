def selection_sort(array):
    """
    Sort a list of items in-place using the selection sort algorithm.

    Finds the smallest element in the unsorted portion and swaps it with
    the first unsorted element. Modifies the original list and returns it.

    Args:
        array: A list of comparable items to sort

    Returns:
        The same list object, sorted in ascending order
    """
    # Iterate through each position that needs to be sorted
    for i in range(len(array)):
        # Find the index of the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        # Only swap if the minimum element is not already in the correct position
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array


# Test cases
def test_selection_sort():
    # Test 1: Unsorted list
    test1 = [20, 3, 14, 1, 5]
    result1 = selection_sort(test1)
    assert result1 == [1, 3, 5, 14, 20]
    assert test1 == [1, 3, 5, 14, 20]  # Verify it modifies in-place
    assert result1 is test1  # Verify it returns the same object
    print("✓ Test 1 passed: [20, 3, 14, 1, 5] → [1, 3, 5, 14, 20]")

    # Test 2: Another unsorted list
    test2 = [83, 4, 24, 2]
    result2 = selection_sort(test2)
    assert result2 == [2, 4, 24, 83]
    assert test2 == [2, 4, 24, 83]
    assert result2 is test2
    print("✓ Test 2 passed: [83, 4, 24, 2] → [2, 4, 24, 83]")

    # Test 3: Larger unsorted list
    test3 = [4, 42, 16, 23, 15, 8]
    result3 = selection_sort(test3)
    assert result3 == [4, 8, 15, 16, 23, 42]
    assert test3 == [4, 8, 15, 16, 23, 42]
    assert result3 is test3
    print("✓ Test 3 passed: [4, 42, 16, 23, 15, 8] → [4, 8, 15, 16, 23, 42]")

    # Test 4: List with duplicates
    test4 = [87, 11, 23, 18, 18, 23, 11, 56, 87, 56]
    result4 = selection_sort(test4)
    assert result4 == [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]
    assert test4 == [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]
    assert result4 is test4
    print(
        "✓ Test 4 passed: [87, 11, 23, 18, 18, 23, 11, 56, 87, 56] → [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]"
    )

    # Test 5: Empty list
    test5 = []
    result5 = selection_sort(test5)
    assert result5 == []
    assert result5 is test5
    print("✓ Test 5 passed: Empty list")

    # Test 6: Single element
    test6 = [1]
    result6 = selection_sort(test6)
    assert result6 == [1]
    assert result6 is test6
    print("✓ Test 6 passed: Single element")

    # Test 7: All identical elements
    test7 = [5, 5, 5, 5]
    result7 = selection_sort(test7)
    assert result7 == [5, 5, 5, 5]
    assert result7 is test7
    print("✓ Test 7 passed: All identical elements (no unnecessary swaps)")

    # Test 8: Already sorted
    test8 = [1, 2, 3, 4, 5]
    result8 = selection_sort(test8)
    assert result8 == [1, 2, 3, 4, 5]
    assert result8 is test8
    print("✓ Test 8 passed: Already sorted list")

    # Test 9: Reverse sorted
    test9 = [5, 4, 3, 2, 1]
    result9 = selection_sort(test9)
    assert result9 == [1, 2, 3, 4, 5]
    assert result9 is test9
    print("✓ Test 9 passed: Reverse sorted list")

    print("\n✅ All tests passed!")


if __name__ == "__main__":
    test_selection_sort()
