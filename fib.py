def fib(n):
    """Return the n-th Fibonacci number, with fib(0) == 0 and fib(1) == 1."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    for i in range(10):
        print(fib(i), end=" ")
    print()
