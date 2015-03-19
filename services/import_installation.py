# -*- coding: utf-8 -*-
import csv
from model.Installation import *

"""
Script permettant d'importer toutes les installations
Utilisation du fichier csv/installations.csv
"""

def num(s):
    """
    Fonction permettant de transformer une string en int.
    Si la conversion echoue pour int, alors elle se fait pour float.
    Pre-condition : la string s doit représenter un int ou un float
    """

    try:
        return int(s)
    except ValueError:
        return float(s)

def importInstallationData():
    """
    Fonction d'importation des installations.
    Parcours du fichier CSV et enregistrement en base de données
    """

    with open('csv/installations.csv', 'rt') as csvfile:
        installationsReader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in installationsReader:
            # numero installation
            numOk = row[1] != "Numéro de l'installation"
            if numOk:
               numero = row[1]
               num(numero)


            # nom installation
            nomOk = row[0] != "Nom usuel de l'installation"
            if nomOk:
               nom = row[0]
               nom = nom.replace('"','')
               if nom is '':
                   nom = 'null'

            # Adress structure ex : 1, rue quartier des pins 44000 Nantes 
            adresseOk = row[6] != "Numero de la voie" and row[7] != "Nom de la voie"
            if adresseOk:
                adresse = row[6]+' '+row[7]
                adresse = adresse.replace('"','')
                if adresse is '':
                    adresse = 'null'

            code_postalOk = row[4] != "Code postal"
            if code_postalOk:
                code_postal = row[4]
                code_postal = code_postal.replace('"','')
                if code_postal is '':
                    code_postal = 'null'
            
            villeOk = row[2] != "Nom de la commune"
            if villeOk:
                ville = row[2]
                ville = ville.strip('"')
                if ville is '':
                    ville = 'null'
            
            # Latitude and longitude

            latitudeOk = row[10] != "Latitude"
            if latitudeOk:
                latitude = row[10]
                num(latitude)

            longitudeOk = row[9] != "Longitude"
            if longitudeOk:
                longitude = row[9]
                num(longitude)

            # Create Installation object
            if numOk and nomOk and adresseOk and code_postalOk and villeOk and latitudeOk and longitudeOk:
                inst = Installation(numero,nom,adresse,code_postal,ville,latitude,longitude)
                inst.save()

    csvfile.close()