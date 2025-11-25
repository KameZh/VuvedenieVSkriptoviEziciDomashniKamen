def sum(a): 
    sum=0 #Tuk zadavame promenlivata (sum) da e ravna na 0, za da izbegnem greshki pri subirane
    for i in range(len(a)): #Tova pravi subirane na elementite v masiva kato vzima razmera na masiva (a) i obhozda vsichki elementi v nego, a "i" e nomera na teku6tiq element
        sum += a[i] #Tuk kum sumata se dobaviq teku6tiq element na tova obhozdane
    return sum #Tuk vrushtame poluchenata suma kum izvikvashtata funkciq

def sumrec(a):
    if len(a) == 0: #Tuk proverqvame dali masiva e prazhen
        return 0
    else:
        return a[0] + sumrec(a[1:]) #Tuk chrez rekursiq vzimame purviq element na masiva i go dobavqme kum rezultata ot izvikvaneto na sumrec s ostanalite elementi v masiva

a = [1, 2, 3, 4, 5] #Tuk definiram masiv s nyakolko chisla
print("Sum iterative:", sum(a)) #Tuk izvikvame iterativnata funkciq sum i printirame rezultata
print("Sum recursive:", sumrec(a)) #Tuk izvikvame rekursivnata funkciq sumrec i printirame rezultata
