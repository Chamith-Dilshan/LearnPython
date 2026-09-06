def recursive_countdown(number):
    if number < 0:
        return
    print(number)
    recursive_countdown(number - 1)
    print(number)


def recursive_countdown_detailed(number):
    print(f"Function call started for number: {number}")
    if number < 1:
        print("Base case reached")
        return
    print(f"Calling recursive_countdown with number: {number - 1}")
    recursive_countdown_detailed(number - 1)
    print(f"Function call completed for number: {number}")


def countup(number):
    if number < 1:
        return []
    count_list = countup(number - 1)
    count_list.append(number)
    return count_list


def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]

    range_numbers = range_of_numbers(start_num, end_num - 1)
    range_numbers.append(end_num)
    return range_numbers


if __name__ == "__main__":
    # recursive_countdown(5)
    recursive_countdown_detailed(3)
    print("\n")
    print(countup(10))
    print("\n")
    print(range_of_numbers(3, 5))
