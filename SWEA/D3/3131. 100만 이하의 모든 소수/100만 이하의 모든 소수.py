MAX = 1000000
is_prime = [False, False] + [True] * (MAX - 1)

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for multiple in range(i * i, MAX + 1, i):
            is_prime[multiple] = False

primes = [str(i) for i in range(2, MAX + 1) if is_prime[i]]
print(' '.join(primes))
