def sum(a):
    sum=0
    for i in range(len(a)):
        sum += a[i]
    return sum

def sumrec(a):
    if len(a) == 0:
        return 0
    else:
        return a[0] + sumrec(a[1:])
    
a = [1, 2, 3, 4, 5]
print("Sum iterative:", sum(a))
print("Sum recursive:", sumrec(a))
