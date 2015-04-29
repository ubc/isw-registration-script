import os
from collections import Counter
from random import randrange

from bottle import request, route, run, static_file, view

from csvkit import writer

import listreader

@route('/')
@view('index')
def index():
	return

@route('/upload', method='POST')
@view('upload')
def process_files():
	# Get the uploaded files
	isw_name = request.forms.get('isw_name')
	ineligible_attended_file = request.files.get('ineligible_attended')
	ineligible_registered_file = request.files.get('ineligible_registered')
	waitlist_file = request.files.get('waitlist')
	registrants_file = request.files.get('registrants')
	if not (file_ext_ok(ineligible_attended_file.filename) and file_ext_ok(ineligible_registered_file.filename)
		and file_ext_ok(waitlist_file.filename) and file_ext_ok(registrants_file.filename)):
		return 'Unfortunately, this thing can only handle CSV or XLS files.'

	# Read all the files into lists of Persons
	ineligible_registered = listreader.readRegistered(listreader.getReader(ineligible_registered_file))
	ineligible_attended = listreader.readAttended(listreader.getReader(ineligible_attended_file))
	registrants = listreader.readRegistrants(listreader.getReader(registrants_file))
	waitlist = listreader.readWaitlist(listreader.getReader(waitlist_file))

	# Remove ineligible registrants
	removed_ineligible_registered = [person for person in registrants if person in ineligible_registered]
	registrants = [person for person in registrants if person not in ineligible_registered]
	removed_ineligible_attended = [person for person in registrants if person in ineligible_attended]
	registrants = [person for person in registrants if person not in ineligible_attended]

	# All registrants are eligible at this point, so add them into the pool once
	pool = []
	for person in registrants:
		pool.append(person)


	# Insert people into the pool however many times they're on the waitlist
	waitlist = Counter(waitlist) # Count how many times each person appears in the waitlist
	registrants_in_waitlist = [person for person in registrants if person in waitlist]
	for person in registrants_in_waitlist:
		numTimesWaitlisted = waitlist[person]
		for i in range(numTimesWaitlisted):
			pool.append(person)

	# randomly assign people in the pool a ranking
	ranking = []
	while len(pool) > 0:
		rand = randrange(len(pool))
		# this person was randomly selected
		randperson = pool[rand]
		ranking.append(randperson)
		# remove this person from the pool
		pool = [person for person in pool if person != randperson]

	# write the output file
	output_file_path = "results/" + isw_name + ".csv"
	with open(output_file_path, 'wb') as output_file:
		outputwriter = writer(output_file)
		outputwriter.writerow(["First Name", "Last Name", "Email"])
		for person in ranking:
			outputwriter.writerow([person.firstname, person.lastname, person.email])

	return dict(ranking=ranking, output_file=output_file_path)

@route('/results/<filename>')
def server_static(filename):
    return static_file(filename, root='results/')

# check that the file extensions are ones we accept
def file_ext_ok(filename):
	name, ext = os.path.splitext(filename)
	if ext not in ('.xls','.csv'):
		return False
	return True

run(host='0.0.0.0', port=8080, debug=True)