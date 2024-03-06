import sys

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)

    return fib_sequence

def get_nth_fibonacci(n):
    fib_sequence = fibonacci(n)
    if n <= 0 or len(fib_sequence) < n:
        return None
    else:
        return fib_sequence[-1]

def main():
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <n>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            print("N must be a non-negative integer.")
            sys.exit(1)

        result = get_nth_fibonacci(n)
        if result is None:
            print("Unable to calculate the Fibonacci number for n =", n)
        else:
            print(f"The {n}-th Fibonacci number is: {result}")

    except ValueError:
        print("N must be a valid integer.")
        sys.exit(1)

if __name__ == "__main__":
    main()
