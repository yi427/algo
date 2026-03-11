def euler_sieve(n):
    spfs = list(range(n + 1))
    primes = []

    for i in range(2, n + 1):
        if spfs[i] == i:
            primes.append(i)

        for p in primes:
            if i * p > n:
                break
            spfs[i * p] = p
            if i % p == 0:
                break

    return spfs
