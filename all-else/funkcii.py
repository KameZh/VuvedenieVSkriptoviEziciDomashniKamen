#zadacha 4 ot kontrolno 1
def purvoto(input_string):
    count = 0
    for ch in input_string:
        if ch != " " and ch != "," and ch != "." and ch != "!" and ch != "?":
            if input_string.count(ch) > count:
                count = input_string.count(ch)
                most_frequent_char = ch
    vtorotodefaktoprint(most_frequent_char)

def vtorotodefaktoprint(char):
    print("The most frequent character is: ", char)

input_string = input("Enter a string to find out what is the most frequent charecter: ")
purvoto(input_string)