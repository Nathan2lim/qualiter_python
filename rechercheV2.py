print("version : v.1")

import time
import random
import matplotlib.pyplot as plt

nbExecution = 10

def generationTab(tailleTableau):
    tab = []
    for i in range(tailleTableau):
        tab.append(random.randint(0, tailleTableau))
    return tab

def trouverUnNb(atrouver, liste):
    for i in range(len(liste)):
        if liste[i] == atrouver:
            return True
    return False

print("Choix du nombre aléatoire")
atrouver = random.randint(0, 10000)
print("Le nombre choisi est", atrouver)

print("Tableau en cours de génération :")
liste = generationTab(100000)

print("Avec", nbExecution, "exécutions :")

tempsExecutions = []  # Liste pour stocker les temps d'exécution

def avecUneMoyenneSurNbExecution(k, atrouver, liste):
    moy = 0
    for i in range(k):
        print("Exécution n°", i)
        depTime = time.time()

        print("Génération d'un tableau")
        liste = generationTab(10000)

        print("Recherche du nombre :", atrouver)
        trouverUnNb(atrouver, liste)

        endTime = time.time()

        tempsExecution = endTime - depTime
        tempsExecutions.append(tempsExecution)

        moy += tempsExecution

        print("L'exécution a pris", tempsExecution, "s")
        print("Le temps moyen est de", moy / (i + 1), "s")
        print("\n")

    moyenneEnTemps = moy / k

    print("Temps passé en secondes en moyenne est de :", moyenneEnTemps)

avecUneMoyenneSurNbExecution(nbExecution, atrouver, liste)

# Création du graphique
plt.plot(tempsExecutions)
plt.xlabel("Test")
plt.ylabel("Temps d'exécution (s)")
plt.show()
