# -*- coding: utf-8 -*-
import csv
import sys
sys.path.append('common/model/')
from Equipement import *
#from model.Equipement import *

"""
Script permettant d'importer tous les equipements
Utilisation du fichier csv/equipements.csv
"""

def num(s):
    '''
    Fonction permettant de transformer une string en int.
    Si la conversion echoue pour int, alors elle se fait pour float.
    Pre-condition : la string s doit représenter un int ou un float
    '''
    try:
        return int(s)
    except ValueError:
        return float(s)

def importEquipementData():
    """
    Fonction d'importation des equipements.
    Parcours du fichier CSV et enregistrement en base de données
    """
    
    with open('csv/equipements.csv', 'rt') as csvfile:
        equipementsReader = csv.reader(csvfile, delimiter=',', quotechar='"')

        # On parcourt toutes les lignes des colonnes en excluant les titres de colonnes.
        # toutes les vérifications sont faites dans "variableOk" où "variable" 
        # représente le nom de l'attribut à tester
        for row in equipementsReader:
            # ID equipement
            idEquipementOk = row[4] != "EquipementId"
            if idEquipementOk:
               id_equipement = row[4]
               num(id_equipement)


            # ID installation
            idInstallationOk = row[2] != "InsNumeroInstall"
            if idInstallationOk:
               id_installation = row[2]
               num(id_installation)

            # Nom usuel de l'equipement
            nomOk = row[5] != "EquNom"
            if nomOk:
                nom = row[5]
                nom = nom.replace('"','')
                if nom is '':
                    nom = 'null'

            # Création de l'objet equipement et sauvegarde en base de données
            if idEquipementOk and idInstallationOk and nomOk:
                equipement = Equipement(id_equipement, id_installation, nom)
                equipement.save()

    csvfile.close()