from libs.bottle import run, view, post, request, route, template, static_file


@route('/static/<filename:path>')
def server_static(filename):
	return static_file(filename, root='static/')

@route('/')
@view('template.tpl')
def blabl():
	context = {'title': "Formulaire", 
				'titre': "Recherche", 
				'ville' : "request.params.ville",
				'sport' : "request.params.sport",
				'equipement' : "request.params.equipement"}
	return (context)

@route('/act')
@view('action.tpl')
def index():
	context = {'title': "Formulaire", 
				'h1': "Resultat", 
				'Colonne1': "Ville", 
				'Colonne2': "Sport", 
				'Colonne3': "Equipement",
				'Colonne3': "Equipement",
				'Colonne3': "Equipement", 
				'ville' : "%s" %request.params.ville,
				'sport' : "%s" %request.params.sport,
				'equipement' : "%s" %request.params.equipement}
	return (context)


run(host='localhost', port=8080, reloader=True, debug=True)