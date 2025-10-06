numbers = [5, 12, 18, 21, 33, 42, 50, 77, 90]
special_numbers = []
for number in numbers:
    if number > 20 and number % 3 == 0 and number % 5 != 0:
        special_numbers.append(number)
print(special_numbers)