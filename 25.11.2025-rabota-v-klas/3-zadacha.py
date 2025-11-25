n = input("Enter a number to find out it's Fibonacci value: ")



def fibonacci_iterative(n):
    if n == 0: return 1
    elif n == 1: return 3
    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    if n < 3:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print("Fibonacci iterative:", fibonacci_iterative(int(n)))
print("Fibonacci recursive:", fibonacci_recursive(int(n)))
