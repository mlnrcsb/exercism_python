def is_isogram(string):
    letters = [] 
    for char in string.lower():
        if char in letters and char not in ' -':
            return False
        letters.append(char)
    return True
            