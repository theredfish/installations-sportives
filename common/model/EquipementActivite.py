# -*- coding: utf-8 -*-
from dict_app import Glob
from GestionDb import *

"""
Classe EquipementActivite ayant la responsabilité de s'ajouter en base de données
"""

class EquipementActivite:
	def __init__(self, id_equipement, id_activite):
		self.id_equipement = id_equipement
		self.id_activite = id_activite

	def save(self):
		"""
		Cette fonction ajoute un nouvel equipement_activite en base de données.
		"""

		add_equipement_activite = ('INSERT IGNORE INTO equipement_activite(id_activite,id_equipement) VALUES ("{}","{}")'.format(self.id_activite, self.id_equipement))

		db = GestionBD(Glob.host, Glob.user, Glob.passwd, Glob.dbName)
		db.executerReq("LOCK TABLES `equipement_activite` WRITE;")
		db.executerReq("SET foreign_key_checks = 0")		
		db.executerReq(add_equipement_activite)
		db.executerReq("SET foreign_key_checks = 1")
		db.commit()
		db.close()

	def __repr__(self):
		"""
		Cette fonction permet d'afficher l'objet de type EquipementActivite
		"""
		return "{} - {}".format(self.id_activite,self.id_equipement)