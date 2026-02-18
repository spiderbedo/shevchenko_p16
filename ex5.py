def primes_under_n() -> set[int]:
    
    """
    Finds all prime numbers less than n using the Eratosthenes algorithm
    Returns:
        set: A set of prime numbers smaller than n.
    """
    
    numbers = input().strip()
    if not numbers:
        return set()
    n = int(numbers)
    if n < 2:
        return set()
    primes = set(range(2, n))
    for i in range(2, int(n ** 0.5) + 1):
        if i in primes:
            multiples = set(range(i * i, n, i))
            primes -= multiples
    return primes


if __name__ == "__main__":
    print(sorted(list(primes_under_n())))
