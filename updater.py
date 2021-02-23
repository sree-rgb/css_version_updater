#!/usr/bin/python
import os
import time
import re
import datetime
PATH_HTML='../portfolio/templates/layout.html'
CSS_FILENAME='main.css'
CSS_PATH='../portfolio/static/main.css'
file=open(PATH_HTML,'r')
# textlines=[line.strip() for line in file.readlines()]
def versionGetter(textlines):
	start=textlines.find('<link rel="stylesheet"')
	end=start+textlines[start:].find('>')
	textlines=textlines[start:end]
	version=textlines[textlines.find('v=')+2:-1]
	return int(version)
def versionIncrement(textlines):
	version=versionGetter(textlines) 
	version+=1
	vindex=textlines.find('v=')+2
	vindex2=vindex+textlines[vindex:].find('"')
	first_half=textlines[:vindex]
	second_half=textlines[vindex2:]
	file=open(PATH_HTML,'w')
	file.write(first_half+str(version)+second_half)
	file.close()
	print('updated',datetime.datetime.now())
	return True
def documentWasUpdated(last_version,current_version):
	return last_version!=current_version
def getCssFile():
	css_file=open(CSS_PATH,'r')
	return css_file.read()
def mainloop():

	while True:
		file=open(PATH_HTML,'r')
		textlines=file.read()
		file.close()
		last_version=getCssFile()
		time.sleep(3)
		current_version=getCssFile()
		if documentWasUpdated(last_version,current_version):
			versionIncrement(textlines)
	



mainloop()

# x = re.search('\<link rel=\"stylesheet\".*', textlines) 
