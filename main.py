import csv
import io
import os
import sys
import geojson
from config import *

def importCSV(name):    
    reader = open(name, mode="r", encoding="utf-8")
    return reader

def readFiles(annee):
    fichierCaracteristiques = importCSV(relPath + '/' + annee + '/' + pathToCaracteristiques)
    fichierLieux = importCSV(relPath + '/' + annee + '/' + pathToLieux)
    fichierUsagers = importCSV(relPath + '/' + annee + '/' + pathToUsagers)
    fichierVehicules = importCSV(relPath + '/' + annee + '/' + pathToVehicules)

    accidentsVelos = dict()
    accidentsVelosNantes = dict()

    # Récupérer les numéros des accidents ayant comme victime cyclistes ou piétons équipés.
    # L'utilisation d'un dictionnaire permet de ne pas avoir de doublons.
    for row in csv.DictReader(fichierVehicules, delimiter=",", quotechar="\""):
        if row["catv"] in filtresVehicules:
            accidentsVelos.update( { row["Num_Acc"] : True } )

    # Récupérer les informations des accidents éligibles.
    for row in csv.DictReader(fichierCaracteristiques, delimiter=",", quotechar="\""):
        if (row["Num_Acc"] in accidentsVelos) and (row["dep"] in filtresDepartements):
            accidentsVelosNantes.update( { row["Num_Acc"] : row } )


    # Génération de la liste pour convertir en GeoJSON
    nbAccidents = len(accidentsVelosNantes)
    geoJsonFeatures = [] # Tableau contenant les Features créées, une Feature étant un objet de la carte (point, trait, polygone)

    for row in accidentsVelosNantes.values():
        try:
            pointAccident = geojson.Feature(geometry=geojson.Point((int(row["long"]) / 100000, int(row["lat"]) / 100000)))

            geoJsonFeatures.append(pointAccident)
        except ValueError:
            print("Error : ")
            print(row)

    listePoints = geojson.FeatureCollection(geoJsonFeatures)
    outputFile = outputPath + "output" + annee + ".json"
    if os.path.exists(outputFile):
        os.remove(outputFile)
    outputJson = open(outputFile, "a")
    outputJson.write(str(listePoints))
    outputJson.close()


    print("En " + annee + ", il y a eu "+str(len(accidentsVelos))+" accidents de la route concernant des cyclistes en France. "+str(len(accidentsVelosNantes))+" en Loire-Atlantique.")


if len(sys.argv) > 1:
    readFiles(sys.argv[1])
else:
    for a in annees:
        readFiles(a)