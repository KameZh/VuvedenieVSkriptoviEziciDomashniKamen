s = input("Enter a string")
output = []
for i in s:
    if i in output:
        output[i] +=1
    elif i not in ".\!\,\?\"":
        output[i] = 1
elem = ""
count = 0
for i, u in output.values():
    if u > count:
        elem = i
        count = u
print(elem, count)