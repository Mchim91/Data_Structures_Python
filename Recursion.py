# Recursion - It's a function that calls itself until it doesn't
# Pseudo code below
# def open_gift_box():
#     if ball:
#         return ball
#     open_gift_box()

# Key-points -> The process of opening each new box is the same
#            -> Each time we open the box we make the problem smaller

# Base case - It's when the function stop to call itself
# Recursive case - It's when the function call itself

# Call stack - 

def funcThree():
    print('3')

def funcTwo():
    funcThree()
    print('2')

def funcOne():
    funcTwo()
    print('1')


funcOne()

# fACTORIAL
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(4))

