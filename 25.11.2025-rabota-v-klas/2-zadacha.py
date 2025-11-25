def flip(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n - i - 1] = a[n - i - 1], a[i]
    return a

def fliprec(a):
    if len(a) <= 1:
        return a
    else:
        return [a[-1]] + fliprec(a[1:-1]) + [a[0]]

a = [1, 2, 3, 4, 5]
print("Flipped iterative:", flip(a.copy()))
print("Flipped recursive:", fliprec(a))