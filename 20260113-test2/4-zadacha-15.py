def is_power_of_three(n):
    if n < 1:
        print("Number must be greater than 0.")
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1

n = int(input("Enter a number: "))
if is_power_of_three(n):
    print(f"{n} is a power of 3.")
else:
    print(f"{n} is not a power of 3.")