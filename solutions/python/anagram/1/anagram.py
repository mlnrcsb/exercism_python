def find_anagrams(word, candidates):
    word = word.lower()
    anagrams = []
    for candidate in candidates:
        candidate_lower = candidate.lower()
        if sorted(candidate_lower) == sorted(word) and candidate_lower != word:
            anagrams.append(candidate)
    return anagrams