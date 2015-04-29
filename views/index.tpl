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
		<h1 class="text-center">ISW Registration Processor</h1>
	</div>

	<form role="form" class="form-horizontal" action="/upload" method="post" enctype="multipart/form-data">
		<div class="form-group">
			<label for="isw_name" class="col-sm-2 control-label"">ISW Name:</label>
			<div class="col-sm-10">
				<input id="isw_name" class="form-control" type="text" name="isw_name" placeholder="E.g.: May 2014" />
				<p class="help-block">This will be the name given to the export file.</p>
			</div>
		</div>
		<div class="form-group">
			<label for="ineligible_attended" class="col-sm-2 control-label">Attended File:</label>
			<div class="col-sm-10">
				<input id="ineligible_attended" type="file" name="ineligible_attended" />
				<p class="help-block">This file lists people who have already attended an ISW.</p>
			</div>
		</div>
		<div class="form-group">
			<label for="ineligible_registered" class="col-sm-2 control-label">Currently Registered File:</label>
			<div class="col-sm-10">
				<input id="ineligible_registered" type="file" name="ineligible_registered" />
				<p class="help-block">This file lists people who are already registered in another ISW.</p>
			</div>
		</div>
		<div class="form-group">
			<label for="waitlist" class="col-sm-2 control-label">Waitlist File:</label>
			<div class="col-sm-10">
				<input id="waitlist" type="file" name="waitlist" />
				<p class="help-block">This file lists people who have been waitlisted for an ISW.</p>
			</div>
		</div>
		<div class="form-group">
			<label for="registrants" class="col-sm-2 control-label">Registrants File:</label>
			<div class="col-sm-10">
				<input id="registrants" type="file" name="registrants" />
				<p class="help-block">This file lists people who wants to attend this ISW.</p>
			</div>
		</div>
		<div class="form-group">
			<div class="col-sm-offset-2 col-sm-10">
				<input type="submit" value="Start upload" class="btn btn-default" />
			</div>
		</div>
	</form>
</div>
</body>
</html>