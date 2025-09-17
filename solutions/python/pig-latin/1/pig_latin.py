def translate(text):
    words = text.split()
    result = []

    for word in words:
        if word[0] in 'aeiou' or word.startswith(('xr', 'yt')):
            result.append(word + 'ay')
        else:
            idx = 1
            while idx < len(word) and word[idx] not in 'aeiouy':
                idx += 1
            if word[idx] == 'u' and word[idx-1] == 'q':
                result.append(word[idx+1:] + word[:idx+1] + 'ay')
            else:
                result.append(word[idx:] + word[:idx] + 'ay')
    return ' '.join(result)