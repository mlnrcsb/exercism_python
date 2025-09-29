def transform(legacy_data):
    mapping = {}
    for point, letters in legacy_data.items():
        for letter in letters:
            mapping[letter.lower()] = point
    return mapping