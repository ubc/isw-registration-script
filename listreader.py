from collections import Counter
import os.path
from random import randrange
import StringIO

from csvkit import reader, sniffer
from csvkit.convert.xls import xls2csv

class Person:
	firstname = ""
	lastname = ""
	email = ""

	def __init__(self, firstname, lastname, email, number='', address1='', address2='',	city='', state='', zip='', country='',
				 institution='', degree='', faculty='', department='', firsttime='', fund=''):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.number = number
		self.address1 = address1
		self.address2 = address2
		self.city = city
		self.state = state
		self.zip = zip
		self.country = country
		self.institution = institution
		self.degree = degree
		self.faculty = faculty
		self.department = department
		self.firsttime = firsttime
		self.fund = fund

	# emails are more unique, check that it matches
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			if self.email.lower() == other.email.lower():
				return True
		return False

	# let the class be hashed
	def __hash__(self):
		return str(self).__hash__()

	# let the class be printed nicely
	def __unicode__(self):
		return "Name: " + self.firstname + " " + self.lastname + " | Email: " + self.email
	def __str__(self):
		return unicode(self).encode('utf-8')

# certain rows should be skipped, such as headers
def skipRow(row):
	if not row:
		return True
	if not row[0]:
		return True
	for col in row:
		if "unnamed" in col: # csvkit inserts these for what it thinks are missing headers
			return True
		# skip what looks like headers, e.g.: if it contains something like "First Name"
		if  col.lower().find("first") >= 0 \
				and col.lower().find("name") >= 0:
			return True
	return False

def readAttended(csvreader):
	ret = []
	for row in csvreader:
		if skipRow(row):
			continue
		person = Person(row[0], row[1], row[2])
		ret.append(person)
	return ret

def readRegistered(csvreader):
	# same format as ISW Attended
	return readAttended(csvreader)

def readWaitlist(csvreader):
	# same format as ISW attended
	return readAttended(csvreader)

def readRegistrants(csvreader):
	ret = []
	for row in csvreader:
		if skipRow(row):
			continue
		elif row[2].lower().find("facilitator") >= 0: # skip facilitators
			continue
		# skip the rest of the file once we've reached summary row
		elif row[0].lower().find("registered") >= 0:
			break
		person = Person(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
		ret.append(person)
	return ret


def getReader(uploadfile):
	file = uploadfile.file
	extension = os.path.splitext(uploadfile.filename)[1]

	csvreader = None
	# make sure to convert excel files
	if extension == '.xls':
		file = StringIO.StringIO(xls2csv(file))
		csvreader = reader(file)
	else:
		dialect = sniffer.sniff_dialect(file.read(4096))
		file.seek(0)
		csvreader = reader(file, dialect=dialect)
	return csvreader
