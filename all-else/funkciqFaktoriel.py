def faktoriel(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n*faktoriel(n-1)

num = int(input("Enter a number to find the factoriel of it: "))
print(faktoriel(num))