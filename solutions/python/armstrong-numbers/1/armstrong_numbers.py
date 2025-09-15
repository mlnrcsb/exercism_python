def is_armstrong_number(number):
    power = len(str(number))
    return number == sum(int(digit)**power for digit in str(number))
