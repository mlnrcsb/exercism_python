def sum_of_multiples(limit, multiples):
    return sum(set(i for n in filter(lambda x: x > 0, multiples) for i in range(1, limit) if not i % n))
