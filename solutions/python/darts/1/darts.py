def score(x, y):
    score = (x**2 + y**2) **(1/2)
    if score <= 1:
        return 10
    if score <= 5:
        return 5
    if score <= 10:
        return 1
    return 0