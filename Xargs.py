def show(*numbers):
    print(numbers)


show(7, 9, 11, 32)      # All are arguments are packed in parentheses


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
