<!DOCTYPE HTML>
<html>
<head>
	<title>
		ISW Registration Processor
	</title>
	<!-- Bootstrap CSS from CDN -->
	<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.1.1/css/bootstrap.min.css">
	<style>
		.main-content
		{
			width: 80%;
		}
	</style>
</head>
<body>
<div class="main-content center-block">
	<div class="page-header">
		<h1 class="text-center">ISW Registration Processor <small>Results</small></h1>
	</div>
	<div class="panel panel-default">
		<div class="panel-body">
			<a href="{{output_file}}" class="btn btn-success center-block">
					Download the Results
			</a>
		</div>
	</div>
	<div class="panel panel-success">
		<div class="panel-heading">
			Randomly Selected Pool Ranking
		</div>
		<div class="panel-body">
			<table class="table table-condensed table-hover">
				<thead>
					<tr>
						<th>#</th>
						<th>First Name</th>
						<th>Last Name</th>
						<th>Email</th>
					</tr>
				</thead>
				% for i, person in enumerate(ranking, start=1):
				<tr>
					<td>{{i}}</td>
					<td>{{person.firstname}}</td>
					<td>{{person.lastname}}</td>
					<td>{{person.email}}</td>
				</tr>
				% end
			</table>
		</div>
	</div>
</div>
</body>
</html>