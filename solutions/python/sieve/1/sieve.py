def primes(n):
    prime = [True] * (n + 1) 
    k = 2
    while k*k <= n:
        if prime[k]:
            for i in range(k*k, n + 1, k):
                prime[i] = False
        k += 1
    return [num for num in range(2, n + 1) if prime[num]]