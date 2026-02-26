input_string = input("Enter a string to find out what is the most frequent charecter: ")
count = 0
for ch in input_string:
    if ch != " " and ch != "," and ch != "." and ch != "!" and ch != "?":
        if input_string.count(ch) > count:
            count = input_string.count(ch)
            most_frequent_char = ch
print("The most frequent character is: ", most_frequent_char)