n = input("Enter n: ")
nums = []
for i in range(int(n)):
    num = input(f"Enter number {i+1}: ")
    nums.append(int(num))
a = 0
for i in nums:
    if i%2 == 1 and i > a:
        a = i
if a:
    print(a)
else:
    print("no odds")