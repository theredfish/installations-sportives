# -*- coding: utf-8 -*-
from model.GestionDb import *
from config.dict_app import Glob

"""
Classe Equipement ayant la responsabilité de s'ajouter en base de données
"""

class Equipement:
	def __init__(self, id_equipement, id_installation, nom):
		self.id_equipement = id_equipement
		self.id_installation = id_installation
		self.nom = nom

	def save(self):
		"""Cette fonction permet d'ajouter un nouvel équipement en base de données"""

		add_equipement = ('INSERT INTO equipement VALUES ("{}","{}","{}")'.format(self.id_equipement, self.id_installation, self.nom))
		db = GestionBD(Glob.host, Glob.user, Glob.passwd, Glob.dbName)
		db.executerReq("LOCK TABLES `equipement` WRITE;")
		db.executerReq("SET foreign_key_checks = 0")		
		db.executerReq(add_equipement)
		db.executerReq("SET foreign_key_checks = 1")
		db.commit()
		db.close()

	def __repr__(self):
		"""Cette fonction permet d'afficher l'objet de type Equipement"""
		
		return "{} - {} - {}".format(self.id_equipement,self.id_installation,self.nom)