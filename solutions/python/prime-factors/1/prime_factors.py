def factors(value):
    prime_factors = []

    while not value % 2:
        prime_factors.append(2)
        value //= 2

    n = 3
    while n**2 <= value:
        while not value % n:
            prime_factors.append(n)
            value //= n
        n += 2

    if value > 1:
        prime_factors.append(value)
    return prime_factors