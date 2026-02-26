data = {"name" : "Atanas",
        "age" : 84,
        "teacher" : True}
print(data["age"])
for key in data:
    print(key, data[key])

for k, v in data.items():
    print(k, v)