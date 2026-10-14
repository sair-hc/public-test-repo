def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for d in range(2, int(n**0.5) + 1):
        if n % d == 0:
            return False
    return True


if __name__ == "__main__":
    print([n for n in range(2, 30) if is_prime(n)])
