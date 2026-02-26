a = []
b = []
for i in range(5):
    n = input("Enter a string: ")
    a.append(n)
for el in a:
    if len(el) == 4:
        b.append(el)
print(b)

#nachin ot duskata
a=["test", "Expirin", "Quack", "Hoe", "LOOL"]
b = []
for i in a:
    if len(i) > 4:
        continue
    b.append(i)