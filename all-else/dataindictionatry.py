data = {"name" : "Atanas",
        "age" : 84,
        "teacher" : True}

keys = list(data.keys())

for key in keys:
    print(key)
    data.pop(key)
    print(data)