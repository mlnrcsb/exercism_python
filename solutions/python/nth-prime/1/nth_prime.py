def prime(n):
    if n < 1:
        raise ValueError('there is no zeroth prime')
    if n == 1:
        return 2
    primes = [2]
    k = 1
    while len(primes) < n:
        k += 2
        
        for prime in primes:
            if not k % prime:
                break
        else:
            primes.append(k)
    return k