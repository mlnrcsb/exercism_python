def is_valid(isbn):
    isbn = isbn.replace('-', '')
    numbers = '0123456789'

    if len(isbn) != 10:
        return False
    
    if isbn[-1] in numbers:
        last_digit = int(isbn[-1])
    elif isbn[-1] == 'X':
        last_digit = 10
    else:
        return False
    
    digit_total = 0
    for i in range(10, 1, -1):
        digit = isbn[10-i]
        if digit not in numbers:
            return False
        digit_total += int(digit) * i
        
    digit_total += last_digit
    return not digit_total % 11