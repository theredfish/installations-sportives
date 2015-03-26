# -*- coding: utf-8 -*-
class Glob:
	"""Espace de noms pour les variables et fonctions <pseudo-globales>"""
	
	dbName = "projet_python"
	user = "root"
	passwd = "toor"
	host = "127.0.0.1"

	# Structure de la base de donnees sous la forme d'un dictionnaire avec tables et champs
	dicoT = {"installation":[('id_install',"k","PK cle"),
							 ('nom', 255, "nom"),
							 ('adresse', 255, "adresse"),
							 ('code_postal', 255, "code postal"),
							 ('ville', 255, "ville"),
							 ('latitude', "d", "latitude position"),
							 ('longitude', "d", "longitude position")],
			 "equipement":[('id_equip',"k","PK cle"),
			 			   ('id_install', "f", "FK cle installation", "installation(id_install)"),
						   ('nom', 255, "nom")],
   			 "activite":[('id_activite',"k","cle primaire"),
						 ('nom', 255, "nom")],
			 "equipement_activite":[('id', "ki", "PK cle"),
			 						('id_equipement',"f", "FK cle equipement", "equipement(id_equip)"),
			 						('id_activite', "f", "FK cle activite", "activite(id_activite)")]

	}