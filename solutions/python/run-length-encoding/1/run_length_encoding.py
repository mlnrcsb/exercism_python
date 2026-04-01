import re

def encode(data):
    if not data:
        return ''
    current_char = data[0]
    char_count = 1
    compressed_data = ''
    for char in data[1:]:
        if char != current_char:
            count_encoding = str(char_count) if char_count > 1 else ''
            compressed_data += count_encoding + current_char
            current_char, char_count = char, 0
        char_count += 1

    if char_count > 1:
        compressed_data += str(char_count) + data[-1]
    else:
        compressed_data += data[-1]
    return compressed_data


def decode(data):
    if not data:
        return ''

    decompressed_data = ''  
    pattern = r'(\d*)([a-zA-Z\s])'

    for count, char in re.findall(pattern, data):
        count = int(count) if count else 1
        decompressed_data += count * char
    return decompressed_data