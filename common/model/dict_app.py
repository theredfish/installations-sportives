# -*- coding: utf-8 -*-
class Glob:
	'''
	================================================
			Introduction
	================================================
	Ce dictionnaire est une représentation
	de la base de données. De façon générale
	on retrouve pour chaque entrée le nom de
	la table. Pour chaque entrée une description
	est fournie : 
		- nom du champ, 
		- type, 
		- commentaire.

	Pour la gestion des clés étrangères la gestion
	est quelque peu différente : 
		- nom du champ, 
		- type, 
		- nom cle etrangere
		- reference cle etrangere

	================================================
			Les types utilisés
	================================================
	k : primary key (INTEGER UNSIGNED)
	f : foreign key (INTEGER UNSIGNED)
	i : INTEGER UNSIGNED
	d : DOUBLE
	ki : INTEGER UNSIGNED AUTO_INCREMENT
	255 : VARCHAR(255)

	================================================
			Configuration de la connexion
	================================================
	Au besoin il suffit de changer les informations
	de connexion à la base de données.

	dbName : nom de la base de données
	user : identifiant de l'utilisateur
	passwd : mot de passe de l'utilisateur
	host : hôte de la base de données
	'''
	
	dbName = "projet_python"
	user = "root"
	passwd = "toor"
	host = "127.0.0.1"
	
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