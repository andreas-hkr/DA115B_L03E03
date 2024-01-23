def fibonacci_1(n):                 # Extra memory
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]


def fibonacci_2(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    for _ in range(2, n + 1):
        tmp = current
        current = previous + current
        previous = tmp

    return current


def fibonacci(n):
    if n <= 1:      # Base case
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


# Fibonacci = 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
def main():
    for i in range(50):
        print(f'{i:3d} : {fibonacci(i)}')


if __name__ == '__main__':
    main()
