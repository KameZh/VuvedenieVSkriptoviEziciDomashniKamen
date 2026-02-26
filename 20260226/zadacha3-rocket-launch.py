import time 
import random

seconds = int(random.randint(5, 20))
print(f"Rocket will launch in {seconds} seconds...")
for i in range(seconds, -1, -1):
    if i == 0:
        print("Rocket lauching!")
    else:
        print(f"{i} seconds remaining...")
        time.sleep(1)
    