grades = [95, 82, 67, 54, 100, 73, 88, 42]
excellent = []
good = []
pas = []
fail = []
for grade in grades:
    if grade >=90:
        excellent.append(grade)
    if grade >=70 and grade <=89:
        good.append(grade)
    if grade >=50 and grade <=69:
        pas.append(grade)
    if grade <50:
        fail.append(grade)
print("Excellent grades:", excellent)
print("Good grades:", good)
print("Pass grades:", pas)
print("Fail grades:", fail)