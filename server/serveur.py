# -*- coding: utf-8 -*-
from libs.bottle import run, view, post, request, route, template, static_file
import sys
sys.path.append('../common/model/')
from GestionDb import *
from dict_app import Glob

@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root='static/')

@route('/')
@view('template.tpl')
def index():
	context = {'title': "Formulaire", 
				'titre': "Recherche", 
				'ville' : "request.params.ville",
				'sport' : "request.params.sport",
				'equipement' : "request.params.equipement"}
	return (context)

@route('/resultat')
# @view('resultat.tpl')
def resultat():
	# Objet base de données
	db = GestionBD(Glob.host, Glob.user, Glob.passwd, Glob.dbName)
	
	# Récupération des informations issues du formulaire
	ville = request.GET.get('ville')
	sport = request.GET.get('sport')
	equipement = request.GET.get('equipement')
	# idEquipement = request.GET.get('idEquipement')
	# adresse = request.GET.get('adresse')
	# codePostal = request.GET.get('codePostal')
	
	# Si la recherche concerne uniquement une ville
	if (ville != '' and sport == '' and equipement == ''):
		req = "select ville, equipement.nom, activite.nom from installation, equipement, equipement_activite, activite where installation.id_install = equipement.id_install and equipement.id_equip = equipement_activite.id_equipement and equipement_activite.id_activite = activite.id_activite "
	
	# Si la recherche concerne uniquement un sport
	elif (ville == '' and sport != '' and equipement == ''):
		req = "select ville, equipement.nom, activite.nom from installation, equipement, equipement_activite, activite where installation.id_install = equipement.id_install and equipement.id_equip = equipement_activite.id_equipement and equipement_activite.id_activite = activite.id_activite and activite.nom like '%"+sport+"%' "
	
	# Si la recherche concerne uniquement un equipement
	elif (ville == '' and sport == '' and equipement != ''):
		req = "select ville, equipement.nom, activite.nom from installation, equipement, equipement_activite, activite where installation.id_install = equipement.id_install and equipement.id_equip = equipement_activite.id_equipement and equipement_activite.id_activite = activite.id_activite and equipement.nom like '%"+equipement+"%' "

	# Si la recherche concerne une ville et un sport	
	elif (ville != '' and sport != '' and equipement == ''):
		req = "select ville, equipement.nom, activite.nom from installation, equipement, equipement_activite, activite where installation.id_install = equipement.id_install and equipement.id_equip = equipement_activite.id_equipement and equipement_activite.id_activite = activite.id_activite and activite.nom like '%"+sport+"%' "

	# Si la recherche concerne une ville, un sport et un équipement
	elif (ville != '' and sport != '' and equipement != ''):
		req = "select ville, equipement.nom, activite.nom from installation, equipement, equipement_activite, activite where installation.id_install = equipement.id_install and equipement.id_equip = equipement_activite.id_equipement and equipement_activite.id_activite = activite.id_activite and activite.nom like '%"+sport+"%' and equipement.nom like '%"+equipement+"%' "

	if (ville != '' or sport != '' or equipement != ''):
		ville_composee = []
		ville_composee = ville.split(" ")
		# On parcourt tous les mots pouvant composer le nom d'une ville
		# On permet d'avoir une recherche plus souple selon l'input
		for mot in ville_composee:
			 req += "and ville like '%"+mot+"%'"
		res = db.lireSelect(req)

		# si checkbox1
			#req += 
		# elif checkbox2

		# elif chbox1 et 2
		return template('resultat',rows=res)
	else:
		return template('error',msg="Vous devez au moins entrer un mot clé pour avoir un résultat.")
	db.close()


@route('/plan')
@view('plan.tpl')
def plan():
	context = {'title' : 'Plan', 'contient' : "Ceci est du text !"}

	return (context)


run(host='localhost', port=8081, reloader=True, debug=True)