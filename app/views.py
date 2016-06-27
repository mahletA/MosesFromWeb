import subprocess
from flask import render_template, flash, redirect
from app import app
from forms import ParamForm
#from moses import mses
from threadsUsed import *
import os
from os import system
from web.api.apimain import RESTAPI
from opencog.atomspace import AtomSpace, types
from opencog.utilities import initialize_opencog
from opencog.type_constructors import *
from opencog.scheme_wrapper import scheme_eval
import sys

params= ""

#start the genome browser
#gthread=genomeThread()
#gthread.start()



# index view function suppressed for brevity
@app.route('/index')
def index():
	return "Hello Mahlet!"


def setParam(data):
	output_file = "param.py"
        of = open(output_file,"w")
	of.write("params = "+"'"+ data +"'")

def openCont():
	system("docker run -d -v /home/mahlet/webCodes:/home/webCodes --name 		userName -t opencog/moses")
	system("docker exec -it userName bash -c 'cd /home/webCodes &&  		python mosesEXEC.py' ")
	system("docker kill userName")
	system("docker rm -f userName")
		
def openBrowser():
	system("cd /home/mahlet/IGV_2.3.77 && ./igv.sh")
	system("")

@app.route('/run', methods=['GET', 'POST'])
def login():
    form = ParamForm()
    if form.validate_on_submit():
		params=form.openid.data
		setParam(params)
		openCont()
		openBrowser()
		#outclass=mses(params)
		#out=outclass.getres()
		#outclass.write()

		return redirect('/result')

    return render_template('moses_run.html', 
                           title='Experiment',
                           form=form)

	

#start the REST api
rest=restThread()
rest.start()

@app.route('/result')

def result():
	return render_template('index.html', 
                           title='Glimpse'
                           )
	#return ('atomspace length ="%s" ' % str(len(atomspace)))







