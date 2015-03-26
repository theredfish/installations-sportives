from libs.bottle import run, view, post, request, route, template, static_file


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
@view('resultat.tpl')
def resultat():
	ville = request.GET.get('ville')
	sport = request.GET.get('sport')
	equipement = request.GET.get('equipement')
	idEquipement = request.GET.get('idEquipement')
	adresse = request.GET.get('adresse')
	codePostal = request.GET.get('codePostal')

	# if ville == None:
	# 	pass

	requestVille = "SELECT * FROM ville"
	requestSport = "SELECT * FROM sport" 
	requestEquipement = "SELECT * FROM equipement"
	requestIdEquipement = "SELECT * FROM idEquipement"
	requestAdresse = "SELECT * FROM adresse"
	requestVille = "SELECT * FROM ville"


	context = {'title': "Formulaire", 
				'h1': "Resultat", 
				'Colonne1': "Ville", 
				'Colonne2': "Sport", 
				'Colonne3': "Equipement",
				'Colonne4': "idEquipement",
				'Colonne5': "adresse", 
				'Colonne6': "codePostal", 
				'ville' : "%s" %ville,
				'sport' : "%s" %sport,
				'equipement' : "%s" %equipement,
				'idEquipement' : "%s" %idEquipement,
				'adresse' : "%s" %adresse,
				'codePostal' : "%s" %codePostal,
				}
	return (context)

@route('/plan')
@view('plan.tpl')
def plan():
	context = {'title' : 'Plan', 'contient' : "Ceci est du text !"}

	return (context)


run(host='localhost', port=8081, reloader=True, debug=True)