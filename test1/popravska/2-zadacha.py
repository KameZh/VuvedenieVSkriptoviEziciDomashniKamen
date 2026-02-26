# I nachin
a = [6, 4, 5, 9, 1]
if a == a.sort():
    print("sorted")
else:
    print("not sorted")


#II nachin
b = [5, 4, 2, 8]
check = True
for i, elem in b:
    if i + 1 > len(b):
        if elem >= a[i+1]:
            check = False
            break
if check:
    print("sorted")
else:
    print("not sorted")

