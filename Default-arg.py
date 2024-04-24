def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="X", child2="Y", child3="Z")


# All the optional parameter should come after the required parameter
# def increment(number, by=5, another):  --- WRONG APPROACH

# def increment(number, another, by=5):
#     return number + by


# print(increment(12, by=6))
