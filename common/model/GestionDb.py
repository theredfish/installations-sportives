# -*- coding: utf-8 -*-
# Code inspiré des sources ci-dessous et adapté à la situation
# https://pythonadventures.wordpress.com/tag/import-from-parent-directory/
# http://fr.wikibooks.org/wiki/Apprendre_%C3%A0_programmer_avec_Python/Gestion_d%27une_base_de_donn%C3%A9es#D.C3.A9crire_la_base_de_donn.C3.A9es_dans_un_dictionnaire_d.27application
import MySQLdb as mdb, sys

"""
Module de la classe GestionBD.
Operations elementaires de base de données.
Connexion, creation, Suppression.
"""

class GestionBD(): 
	
	def __init__(self, host, user, passwd, dbname):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.dbname = dbname
		try:
			self.db = mdb.connect(self.host, self.user, self.passwd, self.dbname, charset='utf8', init_command='SET NAMES UTF8')

		except _mysql.Error, e:
			self.echec = 1
			print "Error %d: %s" % (e.args[0], e.args[1])
			sys.exit(1)
		else:								# Si le try passe alors on exécute ce code
			self.cursor = self.db.cursor()
			self.echec = 0

	def creerTables(self, dicTables):
		"""
		Création des tables décrites dans le dictionnaire <dicTables>.
		"""

		for table in dicTables:            # parcours des clés du dict.
			self.executerReq("SET foreign_key_checks = 0")
			self.executerReq("DROP TABLE IF EXISTS %s" % table)
			req = "CREATE TABLE %s (" % table
			pk = ''
			fk = {}
			references = ''

			for descr in dicTables[table]:
				nomChamp = descr[0]			# libellé du champ à créer
				tch = descr[1]				# type de champ à créer

				if tch =='i':
					typeChamp = 'INTEGER UNSIGNED'
				elif tch =='d':
					typeChamp = 'DOUBLE'
				elif tch == 'k':
					typeChamp = 'INTEGER UNSIGNED'	# champ 'clé primaire'
					pk = nomChamp
				elif tch == 'ki':
					typeChamp = 'INTEGER UNSIGNED AUTO_INCREMENT'	# champ 'clé primaire' (incrémenté automatiquement)
					pk = nomChamp
				elif tch == 'f':
					typeChamp = 'INTEGER UNSIGNED'
					fk[nomChamp] = descr[3]		# reference de la clé étrangère
				else:
					typeChamp ='VARCHAR(%s)' % tch
				req = req + "%s %s, " % (nomChamp, typeChamp)

			# Gestion des différents cas si clé primaire et clé étrangère existent ou non

			# Ni clé primaire ni clé étrangère
			if pk == '' and len(fk) == 0:
				req = req[:-2] + ")"
			
			# Aucune clé primaire et 1 ou n clé étrangère
			elif pk == '' and len(fk) > 0:
				for champ in fk:
					if fk.keys()[-1] == champ:
						req += "CONSTRAINT %s_fk FOREIGN KEY (%s) REFERENCES %s" %(champ, champ, fk[champ])
					else:
						req += "CONSTRAINT %s_fk FOREIGN KEY (%s) REFERENCES %s, " %(champ, champ, fk[champ])
				req += ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
			
			# Uniquement une clé primaire
			elif pk != '' and len(fk) == 0:
				req = req + "CONSTRAINT %s_pk PRIMARY KEY(%s)) ENGINE=InnoDB DEFAULT CHARSET=utf8;" % (pk, pk)
			
			# Clé primaire et 1 ou n clés étrangères
			else:
				req = req + "CONSTRAINT %s_pk PRIMARY KEY(%s), " % (pk, pk)
				# On parcours toutes les clés étrangères
				for champ in fk:
					if fk.keys()[-1] == champ:
						req += "CONSTRAINT %s_fk FOREIGN KEY (%s) REFERENCES %s" %(champ, champ, fk[champ])
					else:
						req += "CONSTRAINT %s_fk FOREIGN KEY (%s) REFERENCES %s, " %(champ, champ, fk[champ])
				req += ") ENGINE=InnoDB DEFAULT CHARSET=utf8;"
			self.executerReq(req)
		self.executerReq("SET foreign_key_checks = 1")

	def executerReq(self, req):
		"""
		Exécution de la requête <req>, avec détection d'erreur éventuelle
		"""
		
		try:
			self.cursor.execute(req)
		except Exception, err:
			# afficher la requête et le message d'erreur système :
			print "Requête SQL incorrecte :\n%s\nErreur détectée :\n%s"\
			       % (req, err)
			return 0
		else:
			return 1

	def supprimerTables(self, dicTables):
		"""
		Suppression de toutes les tables décrites dans <dicTables>
		Ne peut pas être appelée dans creerTables à cause des checks à 0 et 1
		"""

		self.executerReq("SET foreign_key_checks = 0")
		for table in dicTables.keys():
			req ="DROP TABLE IF EXISTS %s" % table
			self.executerReq(req)
		self.executerReq("SET foreign_key_checks = 1")
		#self.commit()

	def commit(self):
		"""
		Confirme les changements effectues en base de données.
		Commit les opérations
		"""

		if self.db:
			self.db.commit()

	def close(self):
		"""
		Fonction de fermeture de la connexion à la base de données
		"""

		if self.db:
			self.db.close()