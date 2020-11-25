# Script permettant de calculer les approximations de la longueur des pistes cyclables de Nantes.

import os
import csv
import sys
from config import *


# Retourne l'image de x en fonction d'une fonction affine "ax + b"
def GetImage(x, a, b):
    return a * x + b


# Vide et crée un fichier, puis retourne la variable de Stream
def OpenOrCreateCSV(file):
    if os.path.exists(file):
        os.remove(file)
    return open(file, "a")



def GetLongueurPourAnnee(ann):
    lon = str(GetImage(ann, fnX, fnY))
    print("En " + str(ann) + ", la longueur approximative etait de " + lon + "km.")
    return lon


if len(sys.argv) >= 2:
    # Si les arguments "annéedebut" et "annéefin" sont donnés
    CSVFile = OpenOrCreateCSV("./output/longueurs.csv")
    CSVWriter = csv.writer(CSVFile, delimiter=',', quotechar='"')
    CSVWriter.writerow(["annee", "longueur"])

    # Programme Principal
    if len(sys.argv) == 3:

        # On calcule la longueur approximative des pistes cyclables de Nantes pour chaque année entre début et fin.
        for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
            # on inscrit le résultat dans un CSV
            CSVWriter.writerow([str(i), GetLongueurPourAnnee(i)])

    elif len(sys.argv) == 2 :
        # On calcule la longueur approximative des pistes cyclables de Nantes pour cette année
        # Et on inscrit le résultat dans un CSV
        i = int(sys.argv[1])
        CSVWriter.writerow([str(i), GetLongueurPourAnnee(i)])
else :
    print("Il manque des arguments : python longueur.py <anneedebut> [<anneefin>]")
