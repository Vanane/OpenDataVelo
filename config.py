##############################
# Variables de configuration #
##############################
relPath = "./csv"
pathToCaracteristiques = "caracteristiques.csv"
pathToLieux = "lieux.csv"
pathToUsagers = "usagers.csv"
pathToVehicules = "vehicules.csv"
outputPath = "./output"

annees = { "2015", "2016", "2017", "2018", "2019" } # Permet de générer pour ces 5 années si aucune n'est passée en paramètre.

filtresVehicules = {"1", "01", "99"} # 01 est le code pour bicyclettes. 99 est le code pour piétons non-motorisés.
filtresDepartements = {"440", "44"} # Département 44


filtrePointMin = [47.14, -1.74] # Point minimal en-deça duquel les accidents ne sont pas considérés comme étant à Nantes
filtrePointMax = [47.30, -1.44] # Point minimal au-dessus duquel les accidents ne sont pas considérés comme étant à Nantes
# Ces points ont été choisis arbitrairement, de manière à encadrer l'agglomération et une partie de la périphérie.



# Variables qui correspondent à la fonction de régression linéaire de l'évolution de la longueur de spistes de Nantes
fnX = 23.714285714286
fnY = -47307.428571429

