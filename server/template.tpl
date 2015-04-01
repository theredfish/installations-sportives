<html>
	<head>
		<title>{{title}}</title>
		<link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
		<link href="static/main.css" rel="stylesheet" media="screen">
		<script src="static/bootstrap/js/jquery.js"></script>
		<script src="static/bootstrap/js/main.js"></script>
		<script src="static/bootstrap/js/bootstrap.min.js"></script>
	</head>

	<body>
		<div class="jumbotron text-center">
			
			<h1>{{titre}}</h1>

		</div>

		<div class="row menu">
			<!-- main-navbar -->
			<nav class="navbar navbar-default">
			  <div class="container-fluid">
				<!-- Brand and toggle get grouped for better mobile display -->
				<div class="navbar-header">
				  <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
					<span class="sr-only">Toggle navigation</span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				  </button>
				  <a class="navbar-brand" href="/">Recherche</a>
				</div>

				<!-- Collect the nav links, forms, and other content for toggling -->
				<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
				  	<ul class="nav navbar-nav">
						<li>
							<a href="/plan">Plan</a>
						</li>
					</ul>
				</div><!-- /.navbar-collapse -->
			  </div><!-- /.container-fluid -->
			</nav><!-- /main-navbar -->
		</div> <!-- /header -->
		
		<div class="row">
			<div class="col-lg-4 col-md-4">
			</div>
			<div class="col-lg-4 col-md-4 col-xs-12">
				<form method="get" action="resultat">
					<div class="form-group">
						<input id="ville" class="form-control" placeholder="Entrez une ville" type="text" name="ville"/>
						<input id="sport" class="form-control" placeholder="Entrez un sport" type="text" name="sport"/>
						<input id="equipement" class="form-control" placeholder="Entrez un equipement" type="text" name="equipement"/>
						<br>
						
						<ul id="menu-accordeon">
						   <li>
						   		<div id="showmenu"><span class="showMenuArrow hide glyphicon glyphicon-chevron-up"></span><span class="showMenuArrow glyphicon glyphicon-chevron-down"></span> Recherche avancée</div>
									<div class="menuListe">
									    <ul>
								        <li>
								        	<input class="form-control" placeholder="Entrez un id d'équipement" type="text" name="idEquipement"/>
								        </li>
								        <li>
								        	<input class="form-control" placeholder="Entrez une adresse" type="text" name="adresse"/>
								        </li>
								        <li>
								        	<input class="form-control" placeholder="Entrez un code postal" type="text" name="codePostal"/>
								        </li>
								        <li>
								        	<div class="radio">
												<label>
													<input type="radio" value="homme" name="optionsRadios">Homme</input>
												</label>
												<label>
													<input type="radio" value="femme" name="optionsRadios">Femme</input>
												</label>
											</div>
								        </li>
							      	</ul>
								</div>
						   	</li>
						</ul>
						<br>
						
						<div class="col-xs-12 text-center">
							<input id="envoie" class="btn btn-lg btn-primary monBouton" type="submit" value="Envoyer"/>
							<input class="btn btn-lg btn-primary monBouton" type="submit" value="Tout"/>
						</div>
					</div>
				</form>
			</div>
			<div class="col-lg-4">
			</div>
		</div>


	</body>
</html>

