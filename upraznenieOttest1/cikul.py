def sum(num):
    sumeven = 0
    for i in range(0, num+1, 2):
        if i % 2 == 0:
            sumeven += i
    return sumeven

num = 100
print(f"The sum of even numbers from 1 to {num} is:", sum(num))