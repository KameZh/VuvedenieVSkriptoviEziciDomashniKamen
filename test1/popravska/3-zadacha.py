a = [4, 4, 5, 7, 2, 8, 8, 2, 1]

#I nachin
print(set(a))

#II nachin
output = []
for elem in a:
    if elem in output:
        continue
    output.append(elem)
print(output.sort())