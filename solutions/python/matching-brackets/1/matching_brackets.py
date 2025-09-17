def is_paired(input_string):
    parentheses = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in input_string:
        if char in "([{":
            parentheses.append(char)
        elif char in ")]}":
            if not parentheses or parentheses[-1] != pairs[char]:
                return False
            parentheses.pop()

    return not parentheses