LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rows(letter):
    spaces = LETTERS.index(letter)
    n = (2*spaces + 1) // 2
    result = []

    result.append(spaces * ' ' + 'A' + spaces * ' ')
    if n == 0:
        return result
        
    i = 1
    while i < n:
        result.append((spaces - i) * ' ' + LETTERS[i] + (2*i - 1)  * ' ' + LETTERS[i] + (spaces - i) * ' ')
        i += 1
    
    while i > 0:
        result.append((spaces - i) * ' ' + LETTERS[i] + (2*i - 1) * ' ' + LETTERS[i] + (spaces - i) * ' ')
        i -= 1   
    
    result.append(spaces * ' ' + 'A' + spaces * ' ')
    return result