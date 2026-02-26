import random
import math

a = random.randint(1, 20)
b = random.randint(1, 20)
temp = pow(a, 2) + pow(b, 2)
c = math.sqrt(temp)
c = round(c, 2)

print(f"Side a: {a}")
print(f"Side b: {b}")
print(f"The calculated hypotenuse (side c) is: {c}")