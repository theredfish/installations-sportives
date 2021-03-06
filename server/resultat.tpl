﻿<!DOCTYPE html>
<html>
	<head>
		<title>Résultats de la recherche</title>
		<link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
		<link href="static/main.css" rel="stylesheet" media="screen">
		<script src="static/bootstrap/js/jquery.js"></script>
		<script src="static/bootstrap/js/bootstrap.min.js"></script>
	</head>
	<body>
		<div class="jumbotron text-center">
			<h1>Résultat</h1>
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
			  </div><!-- /.container-fluid -->
			</nav><!-- /main-navbar -->
		</div> <!-- /header -->

		<div class="row">
			<div class="col-lg-offset-2 col-md-offset-2 col-sm-offset-2 col-xs-offset-2 col-lg-8 col-md-8 col-sm-8 col-xs-8">
			%if(len(rows) == 0):
				<h1>Aucun résultat trouvé</h1>
			%end
				<table border="1" class="table table-bordered table-hover">
					<thead>
						<tr>
							<th>Ville</th>
							<th>Equipement</th>
							<th>Sport</th>
							%if(adr):
								<th>Code Postal</th>
								<th>Adresse</th>
							%end
							%if(coord):
								<th>Coordonnées</th>
							%end
						</tr>
					</thead>
					<tbody>
						%for row in rows:
							<tr>
								<td>{{row[0]}}</td>
								<td>{{row[1]}}</td>
								<td>{{row[2]}}</td>
								%if(adr):
									<td>{{row[3]}}</td>
									<td>{{row[4]}}</td>
								%end
								%if(coord):
									<td><a href="#">{{row[5]}}</a></td>
								%end
							</tr>
						%end
					</tbody>
				</table>
			</div>
		</div>
	</body>
</html>