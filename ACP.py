
decimals = input("Enter decimal numbers separated by spaces: ")
decimal_numbers = [int(num) for num in decimals.split()]


for decimal_number in decimal_numbers:
    binary_digits = []
    num = decimal_number

    while num > 0:
        remainder = num % 2
        binary_digits.insert(0, remainder)
        num = num // 2

    if not binary_digits:
        binary_digits.append(0)


    binary_string = ''
    for digit in binary_digits:
        binary_string += str(digit)


    print(f"The binary representation of {decimal_number} is {binary_string}")


