def is_pangram(sentence):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    for letter in sentence.lower():
        if letter in letters:
            letters.remove(letter)
    return not letters
