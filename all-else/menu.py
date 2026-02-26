import os
while True:
    os.system('cls')
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    print("Menu for calculator:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Select an option ").lower() #lower osigurqva da e s malki bukvi

    if choice == "1":
        os.system('cls')
        print("Adding...")
        ans = a + b
        print(ans)
        break
    elif choice == "2":
        os.system('cls')
        print("Subractiong...")
        ans = a - b
        print(ans)
        break
    elif choice == "3":
        os.system('cls')
        print("Multiplying...")
        ans = a * b
        print(ans)
        break
    elif choice == "4":
        os.system('cls')
        print("Dividing...")
        ans = a / b
        print(ans)
        break
    elif choice == "exit" or choice == "5":
        os.system('cls')
        print("Exiting...")
        break
    else:
        print("Wrong option")

