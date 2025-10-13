import re
import math

def cipher_text(plain_text):
    c, r = 1, 1
    text = re.sub(r'[^a-z0-9]', '', plain_text.lower())
    if not text:
        return ''
    
    c = math.ceil(math.sqrt(len(text)))
    r = math.floor(math.sqrt(len(text)))
    if r * c < len(text):
        r += 1
    
    rows = [text[i:i+c] for i in range(0, len(text), c)]

    encoded = []
    for i in range(c):
        column = ''.join(row[i] if i < len(row) else ' ' for row in rows)
        encoded.append(column)
    return ' '.join(encoded)