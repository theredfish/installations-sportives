# -*- coding: utf-8 -*-
from model.GestionDb import *
from config.dict_app import Glob

"""
Classe Activite ayant la responsabilité de s'ajouter en base de données
"""

class Activite:
	def __init__(self, id_activite, nom):
		self.id_activite = id_activite
		self.nom = nom

	def save(self):
		"""Cette fonction permet d'ajouter une activite en base de données"""

		add_activite = 'INSERT IGNORE INTO activite VALUES ("{}","{}")'.format(self.id_activite, self.nom)

		db = GestionBD(Glob.host, Glob.user, Glob.passwd, Glob.dbName)
		db.executerReq("LOCK TABLES `activite` WRITE;")
		db.executerReq("SET foreign_key_checks = 0")		
		db.executerReq(add_activite)
		db.executerReq("SET foreign_key_checks = 1")
		db.commit()
		db.close()

	def __repr__(self):
		"""Cette fonction permet d'afficher l'objet de type Activite"""

		return "{} - {}".format(self.id_activite,self.nom)