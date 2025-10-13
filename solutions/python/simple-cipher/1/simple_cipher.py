import random

class Cipher:    
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
    
    def __init__(self, key=None):
        self.key = key or ''.join(random.choice(Cipher.ALPHABET) for _ in range(100))

    @staticmethod
    def shifting(text_character, key_character, available_characters, decoding=False):
        text_index = available_characters.index(text_character)
        key_index = available_characters.index(key_character)
        if decoding:
            key_index = -key_index
        return (text_index + key_index) % len(available_characters)
            
    def encode(self, text):
        if not self.key:
            return text

        alphabet = Cipher.ALPHABET
        key_longer_than_text = self.key * (len(text) // len(self.key) + 1)
        encoded = ''
        for text_char, key_char in zip(text, key_longer_than_text):
            shifted_text_char_idx = Cipher.shifting(text_char, key_char, alphabet)
            encoded += alphabet[shifted_text_char_idx]
        return encoded

    def decode(self, text):
        if not self.key:
            return text

        alphabet = Cipher.ALPHABET
        key_longer_than_text = self.key * (len(text) // len(self.key) + 1)
        decoded = ''
        for text_char, key_char in zip(text, key_longer_than_text):
            shifted_text_char_idx = Cipher.shifting(text_char, key_char, alphabet, True)
            decoded += alphabet[shifted_text_char_idx]
        return decoded
