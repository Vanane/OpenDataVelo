# Programmes exécutables :
  ## Main.py :
  main.py permet de générer un fichier GeoJSON à partir des fichiers CSV contenant les accidents corporels en France pour une année donnée.
  Si l'année n'est pas donnée, alors le programme génère les fichiers des années 2015 à 2019.
  ### Prérequis :
  main.py a été développé sous Python v3.7.3, et utilise la librairie **GeoJSON** v2.5.0. Il est nécessaire de l'installer. Si vous utilisez `python3-pip` en tant que gestionnaire de paquets Python, vous pouvez l'installer à l'aide de cette commande : ```pip3 install geojson==2.5.0```.
  ### Syntaxe :
    python main.py [<annee>]
  ## longueurs.py :
  longueurs.py permet de générer un fichier CSV contenant la longueur approximative des aménagements cyclables de Nantes pour une année donnée, ou pour un intervalle donné.
  ### Prérequis :
  longueurs.py a été développé sous Python v3.7.3.
  ### Syntaxe :
    python longueurs.py <annee> [<anneefin>]


