alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher_map = {a: b for a, b in zip(alphabet, reversed(alphabet))}

def encode(plain_text):
    cleaned = [char.lower() for char in plain_text if char.isalnum()]
    
    transformed = [cipher_map[char] if char.isalpha() else char for char in cleaned]
    
    grouped = ["".join(transformed[i:i+5]) for i in range(0, len(transformed), 5)]
    
    return " ".join(grouped)

def decode(ciphered_text):
    cleaned = [char.lower() for char in ciphered_text if char.isalnum()]
    
    transformed = [cipher_map[char] if char.isalpha() else char for char in cleaned]
    
    return "".join(transformed)