# imports
import csv # Pour parser le csv
import os # Pour la gestion des fichiers
import sys # Pour les arguments en entrée
import geojson # Pour la création de la sortie et le respect des syntaxes de geoJson
from config import * # Importation de la configuration


# Ouvre un fichier et retourne le lecteur de ce fichier
def importCSV(name):    
    reader = open(name, mode="r", encoding="utf-8")
    return reader


# Permet de formater une coordonnée géographique sous la forme chaine "12,345678" pour la convertir en float.
def FormatLatLong(val):
    return float(val.replace(',', '.', 1).strip())


# Traite les données des accidents corporels pour une année donnée en paramètre.
def readFiles(annee):
    # Ouverture des fichiers liés à cette année
    fichierCaracteristiques = importCSV(relPath + '/' + annee + '/' + pathToCaracteristiques)
    fichierLieux = importCSV(relPath + '/' + annee + '/' + pathToLieux)
    fichierUsagers = importCSV(relPath + '/' + annee + '/' + pathToUsagers)
    fichierVehicules = importCSV(relPath + '/' + annee + '/' + pathToVehicules)

    
    accidentsVelos = dict() # Dictionnaire contenant les accidents qui correspondent au critère "Contient au moins une victime vélo"
    accidentsVelosLA = dict()  # Dictionnaire contenant les accidents de cyclistes qui correspondent au critère "En Loire-Atlantique"
    accidentsVelosNantes = dict() # Dictionnaire contenant les accidents de cyclistes à Nantes


    # Récupérer les numéros des accidents ayant comme victime cyclistes ou piétons équipés.
    # L'utilisation d'un dictionnaire permet de ne pas avoir de doublons.
    for row in csv.DictReader(fichierVehicules, delimiter=",", quotechar="\""):
        if row["catv"] in filtresVehicules:
            accidentsVelos.update( { row["Num_Acc"] : True } )


    # Récupérer les informations des accidents éligibles.
    for row in csv.DictReader(fichierCaracteristiques, delimiter=",", quotechar="\""):
        if (row["Num_Acc"] in accidentsVelos) and (row["dep"] in filtresDepartements):
            accidentsVelosLA.update( { row["Num_Acc"] : row } )


    # Récupérer les informations des accidents localisés dans un carré centré sur Nantes
    for row in accidentsVelosLA.values():
        try:
            # Dans les fichiers de 2015 à 2018, latitude et longitude sont stockées en entier à 8 chiffres.
            # Il faut diviser par 10^6 pour obtenir les coordonnées géographiques
            row["lat"] = int(row["lat"]) / 100000
            row["long"] = int(row["long"]) / 100000
        except ValueError:
            # Le problème est que dans les fichiers de 2019, latitude et longitude sont stockées en chaine,
            # qui utilise la virgule comme séparateur, et non le point.
            # Si le premier formatage échoue, alors on sait que c'est un format en chaine de caractère.
            try:
                row["lat"] = FormatLatLong(row["lat"])
                row["long"] = FormatLatLong(row["long"])
            except:
                row["lat"] = 0
                row["long"] = 0
        
        # Si l'accident a eu lieu dans les alentours de Nantes, alors on le considère.
        if(filtrePointMin[0] <= row["lat"] <= filtrePointMax[0] 
        and filtrePointMin[1] <= row["long"]  <= filtrePointMax[1]):
            accidentsVelosNantes.update( { row["Num_Acc"] : row } )



    # Génération de la liste pour convertir en GeoJSON
    geoJsonFeatures = [] # Tableau contenant les Features créées, une Feature étant un objet de la carte (point, trait, polygone)

    # Ensuite, pour chaque ligne filtrée dans le dictionnaire, on génère un point GeoJson.
    for row in accidentsVelosNantes.values():
        pointAccident = geojson.Feature(geometry = geojson.Point((row["long"], row["lat"])))
        geoJsonFeatures.append(pointAccident)

    # On crée un objet Json contenant tous les points créés
    listePoints = geojson.FeatureCollection(geoJsonFeatures)

    # On génère un fichier et on y écrit le Json généré plus haut
    outputFile = outputPath + '/' + "accidents" + annee + ".json"
    if os.path.exists(outputFile):
        os.remove(outputFile)
    outputJson = open(outputFile, "a")
    outputJson.write(str(listePoints))
    outputJson.close()

    #Petit print récapitulatif
    print("En " + annee + ", il y a eu "+str(len(accidentsVelos))+" accidents de la route concernant des cyclistes en France. "+str(len(accidentsVelosNantes))+" en Loire-Atlantique.")


# Programme Principal
if len(sys.argv) > 1:
    if os.path.exists(relPath + '/' + sys.argv[1]):
        readFiles(sys.argv[1])
    else:
        print("Cette année n'existe pas dans les fichiers ! Veuillez l'ajouter.")
else:    
    for a in annees:
        readFiles(a)