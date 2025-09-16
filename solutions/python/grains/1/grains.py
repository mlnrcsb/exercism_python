def square(number):
    if (1 <= number <= 64):
        return 2**(number-1)
    raise ValueError("square must be between 1 and 64")
    
def total():
    value = 0
    for i in range(1, 65):
        value += square(i)
    return value