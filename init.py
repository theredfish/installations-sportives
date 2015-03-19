# -*- coding: utf-8 -*-
from common.model.dict_app import Glob
from common.model.GestionDb import *
from import_csv.import_activite import *
from import_csv.import_equipement import *
from import_csv.import_installation import *

"""
Script permettant d'effectuer des opérations sur la base de données
"""

result = True;
message = "Faites un choix. Choix 1 nécessaire aux autres si non déjà sélectionné avant."

def afficherMessage():
	"""
	Fonction permettant d'afficher les différentes options du Script
	Un choix réalisé executera la fonction associee
	Gestion des opérations d'initialisation de la base de données
	"""

	init_bd = "1] Initialiser la base de données"
	import_activite = "2] Importer les activités en base de données"
	import_equipement = "3] Importer les équipement en base de données"
	import_installation = "4] Importer les installations en base de données"
	quitter = "5] Quitter"
	choix = input(message+"\n"+init_bd+"\n"+import_activite+"\n"+import_equipement+"\n"+import_installation+"\n"+quitter+"\n")
	
	if choix > 0 and choix < 5:
		print(options[choix]())
	else:
		return False

def exec_init_bd():
	""" 
	Fonction permettant d'initialiser la base de données
	Création du schema de base de données
	Ou remise à vide de la base de données si elle est déjà créée
	"""

	datab = GestionBD(Glob.host, Glob.user, Glob.passwd, Glob.dbName)
	datab.creerTables(Glob.dicoT)
	datab.close()
	return "-----> Initialisation des tables de la base données : OK"

def exec_import_activite():
	"""
	Fonction permettant d'executer l'importation des activites depuis un CSV
	"""

	importActivitesData()
	return "-----> Importation des données concernant les activités : OK"

def exec_import_equipement():
	"""
	Fonction permettant d'executer l'importation des equipements depuis un CSV
	"""

	importEquipementData()
	return "-----> Importation des données concernant les équipements : OK"

def exec_import_installation():
	"""
	Fonction permettant d'executer l'importation des installations depuis un CSV
	"""

	importInstallationData()
	return "-----> Importation des données concernant les installations : OK"

options = {1 : exec_init_bd,
           2 : exec_import_activite,
           3 : exec_import_equipement,
           4 : exec_import_installation}

while (True):
	result = afficherMessage()

	if result == False:
		break;