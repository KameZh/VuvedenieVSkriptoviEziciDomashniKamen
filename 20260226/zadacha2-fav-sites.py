import webbrowser

fav = ['https://www.geeksforgeeks.org', 
       'https://www.python.org', 
       'https://www.youtube.com']

print("1. GeeksforGeeks")
print("2. Python")
print("3. YouTube")
choice = int(input("Enter the number corresponding to your choice: "))
if choice == 1:
    webbrowser.open(fav[0])
elif choice == 2:
    webbrowser.open(fav[1])
elif choice == 3:
    webbrowser.open(fav[2])
else:
    print("Invalid choice. Please enter a number between 1 and 3.")