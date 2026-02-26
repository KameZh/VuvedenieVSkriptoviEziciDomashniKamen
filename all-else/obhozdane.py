a=[]
for i in range(5):
    n=input("Enter a number: ")
    a.append(n)
for el in a:
    if int(el)%2==0:
        print(f"{el} is even")
    else:
        print(f"{el} is odd")
