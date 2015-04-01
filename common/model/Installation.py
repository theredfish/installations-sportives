# -*- coding: utf-8 -*-
from dict_app import Glob
from GestionDb import *

"""
Classe Installation ayant la responsabilité de s'ajouter en base de données
"""

class Installation:
	def __init__(self, numero, nom, adresse, code_postal, ville, latitude, longitude): #, adresse, code_postal, ville, latitude, longitude
		self.numero = numero
		self.nom = nom
		self.adresse = adresse
		self.code_postal = code_postal
		self.ville = ville
		self.latitude = latitude
		self.longitude = longitude

	def save(self):
		"""
		Cette fonction permet d'ajouter en base de données une nouvelle installation
		"""

		add_installation = ('INSERT INTO installation VALUES (\
			"{}","{}","{}","{}","{}","{}","{}")'.format(self.numero,
														self.nom,
														self.adresse,
														self.code_postal,
														self.ville,
														self.latitude,
														self.longitude))
		
		db = GestionBD(Glob.host, Glob.user, Glob.passwd, Glob.dbName)
		db.executerReq("LOCK TABLES `installation` WRITE;")		
		db.executerReq(add_installation)
		db.commit()
		db.close()

	def __repr__(self):
		"""
		Cette fonction permet d'afficher l'objet de type Installation
		"""
		
		return "{} - {} - {} - {} - {} - {} - {}".format(self.numero,
														self.nom,
														self.adresse,
														self.code_postal,
														self.ville, 
														self.latitude,
														self.longitude)