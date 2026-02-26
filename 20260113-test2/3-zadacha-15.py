def dividers(n):
    list_of_div = []
    for i in range(2, n):
        if n % i == 0:
            list_of_div.append(i)
    return list_of_div

n = int(input("Enter a number: "))
print(dividers(n))