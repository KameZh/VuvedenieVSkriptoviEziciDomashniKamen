import random
n = random.randint(1, 1000)
print(f"Fucking your pc with {n} files")
for i in range(n):
    filepath = f"C:/Users/samol/Documents/trash-bin-for-files/{i}"
    with open(filepath, "w") as f:
        f.write(f"{i} file")
