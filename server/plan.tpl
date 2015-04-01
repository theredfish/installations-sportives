<!DOCTYPE html>
<html>
	<head>
		<title>{{title}}</title>
		<link href="static/bootstrap/css/bootstrap.min.css" rel="stylesheet" media="screen">
		<link href="static/main.css" rel="stylesheet" media="screen">
	</head>
	<body>

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
			<div class="col-lg-3 col-md-3 col-xs-3">
			</div>
			<div class="col-lg-6 col-md-6 col-xs-6">
				{{contient}}
			</div>
			<div class="col-lg-3 col-md-3 col-xs-3">
			</div>
	</body>
</html>