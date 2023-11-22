print("version : v.1")


import time
import random
import matplotlib.pyplot as plt

nbExection = 10

def generationtab(tailleTableau):
    tab = []
    for i in range(tailleTableau):
        tab.append(random.randint(0,tailleTableau))
    
    return tab

def touverUnNb(atrouver, liste):
    for i in range(len(liste)):
        if liste[i] == atrouver:
            return True
    return False 
    

print("choix du nombre aleatoire")
atrouver = random.randint(0,10000)
print("le nombre choisi est ", atrouver)


print("tableau en cour de generation : ")
liste = generationtab(100000)

print( "avec", nbExection ," execution : ")




def avecUneMoyenneSurNbExecution(k, atrouver, liste):
    
    moy = 0
    i = 0
    
    for i in range(k):
        
        print("execution n° ", i )
        depTime = time.time()
        
        print("generation d'un tableau" )
        liste = generationtab(10000)
        
        print("recherche du nombre : ", atrouver )
        touverUnNb(atrouver,liste)
        
        i += 1 
        endTime = time.time()
        
        
        print("l'execution a pris", endTime-depTime , "s" )

        moy += (endTime - depTime)
        
        print("le temps moyen est de ", moy/i , "s" )
        print("\n")


        
        
    moyenneEnTemps = moy/i
    
    print("Temps passé en secondes en moyenne est de :", moyenneEnTemps)
        

        
        

avecUneMoyenneSurNbExecution(nbExection, atrouver, liste)


        
plt.plot(10)
plt.xlabel("test")
plt.ylabel("testY")

plt.show()