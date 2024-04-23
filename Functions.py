# Two types of function -
# 1 Perform a task
# 2 Return a value

def greet(first_name, last_name):
    print(f"Hi {first_name} and {last_name}")
    print("Welcome to Bangladesh")


greet("Alex", "Asim")


def greet(first_name, last_name):
    return (f"Hi {first_name} and {last_name}")


message = greet("Aman", "Bill")
print(message)


# # xargs (tuple)
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))
