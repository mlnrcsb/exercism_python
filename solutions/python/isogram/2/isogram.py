def is_isogram(string):
    cleaned = string.lower().replace(' ', '').replace('-', '')
    return len(cleaned) == len(set(cleaned))