def score(word):
    score_system = {
        'AEIOULNRST' : 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10
    }
    return sum(score_system[category] for category in score_system.keys() for char in word.upper() if char in category)
    
