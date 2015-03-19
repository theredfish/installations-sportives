<html>
	<head>
		<title>{{title}}</title>
		<link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
	</head>

	<body>
		<div class="jumbotron text-center">
			<h1>{{titre}}</h1>
		</div>
		
		<div class="row">
			<div class="col-lg-4 col-md-4 col-xs-4">
			</div>
			<div class="col-lg-4 col-md-4 col-xs-4">
				<form method="get" action="act">
					<div class="form-group">
						<input class="form-control" placeholder="Enter une ville" type="text" name="ville"/>
						<input class="form-control" placeholder="Enter un sport" type="text" name="sport"/>
						<input class="form-control" placeholder="Enter un equipement" type="text" name="equipement"/>
						<div class="radio">
							<label>
								<input type="radio" value="homme" name="optionsRadios">Homme</input>
							</label>
							<label>
								<input type="radio" value="femme" name="optionsRadios">Femme</input>
							</label>
						</div>
						<div class="row">
							<div class="col-lg-9 col-md-9 col-xs-9">
							</div>
							<div class="col-lg-3 col-md-3 col-xs-3">
								<input class="btn btn-lg btn-primary" type="submit" value="Envoyer"/>
							</div>
					</div>
				</form>
			</div>
			<div class="col-lg-4 col-md-4 col-xs-4">
			</div>
		</div>
	</body>
</html>

