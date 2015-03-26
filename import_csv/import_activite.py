# -*- coding: utf-8 -*-
import csv
import sys
sys.path.append('common/model/')
from Activite import *
from EquipementActivite import *
# from common.model.Activite import *
# from model.EquipementActivite import *

"""
Script permettant d'importer toutes les activites
Utilisation du fichier csv/activites.csv
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

def importActivitesData():
    """
    Fonction d'importation des equipements.
    Parcours du fichier CSV et enregistrement en base de données
    """

    with open('csv/activites.csv', 'rt') as csvfile:
        activitesReader = csv.reader(csvfile, delimiter=',', quotechar='"')

        # On parcourt toutes les lignes des colonnes en excluant les titres de colonnes.
        # toutes les vérifications sont faites dans "variableOk" où "variable" 
        # représente le nom de l'attribut à tester
        for row in activitesReader:
        	
            # ID activité
            idActiviteOk = row[4] != "Activité code" and row[4] != ""
            if idActiviteOk:
                id_activite = row[4]
                id_activite.strip()
                num(id_activite)

        	# Nom usuel de l'activite
            nomOk = row[5] != "Activité libellé"
            if nomOk:
                nom = row[5]
                nom = nom.replace('"','')
                if nom is '':
                    nom = 'null'

             # On peuple la table Equipement_Activite
            idEquipOk = row[2]  != "Numéro de la fiche équipement" and row[2] != ""
            
            if idActiviteOk and idEquipOk:
                id_equip = row[2]
                id_equip.strip()
                num(id_equip)
                newEquipAct = EquipementActivite(id_equip,id_activite)
                newEquipAct.save()

            # Création de l'objet activite et sauvegarde en base de données
            if idActiviteOk and nomOk:
                activite = Activite(id_activite, nom)
                activite.save()

    csvfile.close()