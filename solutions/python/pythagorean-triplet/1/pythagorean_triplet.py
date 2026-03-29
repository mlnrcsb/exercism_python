def triplets_with_sum(number: int):
    triplets = []
    for a in range(1, number//3):
        for b in range(a + 1, number//2):
            c = number - b - a
            if a*a + b*b == c*c:
                triplets.append([a, b, c])
    return triplets