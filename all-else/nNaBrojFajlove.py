n = int(input("How many files would you like to trash your pc with: "))
for i in range(n):
    filename = f"C:/Users/samol/Documents/trash-bin-for-files/file_{i}.txt"
    f = open(filename, "w") 
    f.write(f"This is file number {i}")
    f.close()