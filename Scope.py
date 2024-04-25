message = 'a'


def greet(name):
    # Try not to use this type of Modification or Declaration, it is a Bad practise
    global message
    message = 'b'


greet('Sourav')
print(message)
