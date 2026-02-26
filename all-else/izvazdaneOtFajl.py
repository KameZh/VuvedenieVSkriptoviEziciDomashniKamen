filename = "C:/Users/samol/Desktop/tekst.txt"
filename2 = "C:/Users/samol/Desktop/izvazdane.txt"
with open (filename,"r", encoding="utf-8") as f:
    data = f.readlines()
output = []
for i, line in enumerate(data):
    if (i+1) % 2 == 0:
        output.append(line)
print(output)
with open (filename2, "w", encoding="utf-8") as f:
    f.writelines(output)
