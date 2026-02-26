a = []
odd = []
biggest = 0
for i in range(5):
    user_input = input(f"Enter a number in position {i+1}: ")
    a.append(user_input)
for j in a:
    if int(j)%2 == 1:
        odd.append(j)
        if int(j) > biggest:
            biggest = int(j)
g = max(odd)
print("The biggest odd number is: ", g)