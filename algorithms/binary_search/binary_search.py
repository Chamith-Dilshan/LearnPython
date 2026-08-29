# Binary Search

# Time Complexity: O(log n)
# Space Complexity: O(1)
# A binary search algorithm finds the position of a specified value within a sorted array.
# It compares the target value with the middle element of the array, and if they are not equal,
# it divides the search space in half. This process is repeated until the target value is found.


def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1

    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return path_to_target, f"Value found at index {mid}"
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return [], "Value not found"


print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))
