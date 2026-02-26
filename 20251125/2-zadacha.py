def flip(a):
    n = len(a) #Tuk zadavame proimenlivata (n) da e ravna na duljinata na masiva (a)
    for i in range(n // 2): #Obhozda masiva do negovata sreda (pri4inata za izpolzvaneto na // e che ako masiva e s nechetna duljina, sredniqt element ne trqbva da se premestva)
        a[i], a[n - i - 1] = a[n - i - 1], a[i] #Tuk razmenqme mestata na teku6tiya element s negoviq simetri4en element ot drugata strana na masiva
    return a #Vru6tame obarnatiq masiv kum izvikva6tata funkciq

def fliprec(a):
    if len(a) <= 1: #Ako masiva e prazen ili ima samo edin element, go vru6tam kakto si e bez promqna
        return a #Vru6tame masiva kakto si e
    else: #ili
        return [a[-1]] + fliprec(a[1:-1]) + [a[0]] #Tuk vzimame posledniq element na masiva i go dobavqme kum rezultata ot izvikvaneto na fliprec s ostanalite elementi bez purviq i posledniq, sled koeto dobavqme purviq element na masiva na kraq
        #Realno poglednato gledame masiva ot vun i razmenqme purviq i posledniq element, dokato ne stignem do sredata
a = [1, 2, 3, 4, 5]
print("Flipped iterative:", flip(a.copy())) #Izpolzvame a.copy(), za da ne promenim originalniq masiv
print("Flipped recursive:", fliprec(a)) #Tuk ne e nuzno da izpolzvame copy, za6toto rekursivnata funkciq ne promenq originalniq masiv