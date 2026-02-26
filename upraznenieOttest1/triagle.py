def triangle(n):
    if n != 0:
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print("Invalid input: n must be greater than 0.")

num = int(input("Enter the number of rows for the triangle: "))
triangle(num)