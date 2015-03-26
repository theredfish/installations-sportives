<!DOCTYPE html>
<html>
	<head>
		<title>{{title}}</title>
		<link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
		<link href="static/main.css" rel="stylesheet" media="screen">
		<script src="static/bootstrap/js/jquery.js"></script>
		<script src="static/bootstrap/js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="jumbotron text-center">
			<h1>{{h1}}</h1>
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
							<a href="/resultat">Résultat</a>
						</li>
						<li>
							<a href="/plan">Plan</a>
						</li>
					</ul>
				</div><!-- /.navbar-collapse -->
			  </div><!-- /.container-fluid -->
			</nav><!-- /main-navbar -->
		</div> <!-- /header -->

		<div class="row">
			<div class="col-lg-2 col-md-2 col-xs-2">
			</div>
			<div class="col-lg-8 col-md-8 col-xs-8">
				<table class="table table-bordered table-hover">
					<tr>
						<th>{{Colonne1}}</th>
						<th>{{Colonne2}}</th>
						<th>{{Colonne3}}</th>
						<th>{{Colonne4}}</th>
						<th>{{Colonne5}}</th>
						<th>{{Colonne6}}</th>
					</tr>
				    <tr>
					    <td>{{ville}}</td>
					    <td>{{sport}}</td>
					    <td>{{equipement}}</td>
					    <td>{{idEquipement}}</td>
					    <td>{{adresse}}</td>
					    <td>{{codePostal}}</td>
					</tr>
				</table>
			</div>
			<div class="col-lg-2 col-md-2 col-xs-2">
			</div>
	</body>
</html>
