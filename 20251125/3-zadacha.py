n = input("Enter a number to find out it's Fibonacci value: ") #Vzimame vhod ot potrebitelq

def fibonacci_iterative(n):
    if n == 0: return 1 #Definirame bazovite sluchai
    elif n == 1: return 3 #Definirame bazovite sluchai
    a, b = 1, 1  #Parvite dve chisla v redicata na Fibona4i (moje da se zapochva ot 0 i 1, no samiq Fibona4i tvurdi che redicata mu zapo4va ot 1 i 1(po informaciq ot wikipedia))
    for _ in range(2, n): #Obhozdame ot 2 do n (tuk izpolzvame _ kato promenliva, za6toto ne ni interesuva stoinostta)
        a, b = b, a + b #Vsqko novo chislo e sudurzanieto na dvete predishni chisla
    return b #Vru6tame n-toto chislo v redicata


def fibonacci_recursive(n):
    if n < 3:
        return 1 #Definirame bazovite sluchai
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2) #Rekursivno iz4islyavame n-toto chislo kato subirame dvete predishni chisla 

print("Fibonacci iterative:", fibonacci_iterative(int(n))) #izvukvane na iterativnata funkciq i izpolzvame int(n), za6toto vhodut e kato string
print("Fibonacci recursive:", fibonacci_recursive(int(n))) #su6toto vuzi i tuk
