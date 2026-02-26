def triangle(n):
    for i in range(n+1):
        for j in range(i+1):
            print(j, end = " ")
        print()

num = int(input("Enter a number: "))
triangle(num)