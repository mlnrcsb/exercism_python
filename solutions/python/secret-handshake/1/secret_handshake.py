def commands(binary_str):
    sequence = ['jump', 'close your eyes', 'double blink', 'wink']
    
    handshake = []
    for i in range(1 ,len(binary_str)):
        if binary_str[i] == '1':
            handshake.append(sequence[i - 1])
    if binary_str[0] == '0':
        handshake.reverse()
    return handshake