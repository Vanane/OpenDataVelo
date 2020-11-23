# Script permettant de calculer les approximations de la longueur des pistes cyclables de Nantes.

import os
import io
import csv
import sys


fnX = 23.7
fnY = -47307


def GetImage(annee, x, y):
    return x * annee + y


def OpenOrCreateCSV(file):
    if os.path.exists(file):
        os.remove(file)
    return open(file, "a")


# Programme Principal
if len(sys.argv) == 3:
    CSVFile = OpenOrCreateCSV("./output/longueurs.csv")
    CSVWriter = csv.writer(CSVFile, delimiter=',', quotechar='"')
    CSVWriter.writerow(["annee", "longueur"])

    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1):
        ann = str(i)
        lon = str(GetImage(i, fnX, fnY))
        # CSVWriter.writerow([ann, lon])
        CSVWriter.writerow([str(i), str(GetImage(i, fnX, fnY))])
        print("En " + ann + ", la longueur approximative etait de " + lon + "km.")
elif len(sys.argv) == 2 :
    CSVFile = OpenOrCreateCSV("./output/longueurs.csv")
    CSVWriter = csv.writer(CSVFile, delimiter=',', quotechar='"')
    CSVWriter.writerow(["annee", "longueur"])

    i = int(sys.argv[1])
    ann = str(i)
    lon = str(GetImage(i, fnX, fnY))
    CSVWriter.writerow([str(i), str(GetImage(i, fnX, fnY))])
    print("En " + ann + ", la longueur approximative etait de " + lon + "km.")
else :
    print("Il manque des arguments : python longueur.py <anneedebut> <anneefin>")

