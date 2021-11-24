# TO DO apreķinam barbutibu
import math


def salidzinājums(x,y):
    return x > y

def varbūtiba(a ,z):
    return a/z * 100

def kombinācijas(x):
    return math.factorial(x)

# TO DO salidzinaim varbūtiba

# TO DO veiksmigakais speles komunikacija aprekināsana

# TO DO apreķinašim litotajs ievait
if __name__ == '__main__':
    #input no pirmas speles, dzivi mainibu: cikOne, nocikOne
    #ievadies parbaude
    cikOne = int(input("x1"))
    nocikOne = int(input("x2"))


    if cikOne > nocikOne:
        print()
        exit(0)

    cikTwo = int(input("y1"))
    nocikTwo = int(input("y2"))
    if int(cikTwo) > int(nocikTwo):
        print("nav iepejams")
        exit(0)

    pirma = varbūtiba(cikOne , nocikOne)
    print("Pirma vetibība ir", round(pirma), "%")

    otra = varbūtiba(cikTwo, nocikTwo)
    print("otra vetibība ir", round(otra), "%")

    thebest = (salidzinājums, otra)
    if thebest == True:
        komb1 = kombinācijas(cikOne)
        print(cikOne, "Tu vari izvēleties", komb1, "dažad kombinācijas")
    if thebest == False:
        komb2 = kombinācijas(cikTwo)
        print(cikTwo, "Tu vari izvēleties", komb2, "dažad kombinācijas")
    else:
        print("Error")
        exit()

