"""
Luhn Algorithm Credit Card Validator

The Luhn algorithm (also called mod-10) is a checksum formula used to validate
credit card numbers and detect simple errors in typing or transmission. It's
the international standard (ISO/IEC 7812-1) for credit card validation.

WHERE TO USE:
- E-commerce platforms (payment processing validation)
- Banking applications (card verification)
- Form validation (client-side or server-side)
- POS (Point of Sale) systems
- Payment gateways

HOW IT WORKS:
1. Process digits from right to left
2. Double every second digit (starting from position 2 from the right)
3. If a doubled digit > 9, subtract 9 from it
4. Sum all the digits
5. If the sum is divisible by 10, the card number is valid

IMPORTANT: This only validates the *format* of a card number. It does NOT:
- Check if the card is active or has funds
- Verify the card belongs to the person using it
- Prevent fraud (use with proper security measures)
"""


def verify_card_number(value):
    # Remove spaces and dashes
    # digit_only = value.replace(" ", "").replace("-", "")

    # Remove all non-digit characters
    digit_only = "".join(char for char in value if char.isdigit())

    # Check if we have a valid number
    if not digit_only or len(digit_only) < 13:
        return "INVALID!"

    new_values = []

    # Process from right to left (reverse the string)
    for index, digit in enumerate(reversed(digit_only)):
        digit_value = int(digit)

        # Every second digit from the right (index 1, 3, 5, ...)
        if index % 2 == 1:
            digit_value *= 2
            # If doubled value > 9, subtract 9 (equivalent to summing digits)
            if digit_value > 9:
                digit_value -= 9
        new_values.append(digit_value)

    sum_value = sum(new_values)

    if sum_value % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


def main():
    print(verify_card_number("453914889"))  # Test 1
    print(verify_card_number("4111-1111-1111-1111"))  # Test 2
    print(verify_card_number("4111 1111 1111 1111"))  # Test 3
    print(verify_card_number("4111--1111||1111>>1111"))  # Test 4 (any characters)
    print(verify_card_number("invalid"))  # Test 5 (no digits)
    print(verify_card_number("12"))  # Test 6 (too short)

    card_number = input("Enter your card number: ")
    print(verify_card_number(card_number))


if __name__ == "__main__":
    main()
