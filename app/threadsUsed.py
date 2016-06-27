import threading
import subprocess

from web.api.apimain import RESTAPI
from opencog.atomspace import AtomSpace, types
from opencog.utilities import initialize_opencog
from opencog.type_constructors import *
from opencog.scheme_wrapper import scheme_eval

class genomeThread(threading.Thread):
	def run(self):
		python_bin = "/home/mahlet/api-client-python-master/localserver_libs/bin/python"
		script_file = "/home/mahlet/api-client-python-master/localserver.py"
		subprocess.Popen([python_bin, script_file])




class restThread(threading.Thread):
	def run (self):

		atomspace=AtomSpace()
		scheme_clear=\
			"""
			(clear)
			"""
		scheme_code=\
				"""
				(load-scm-from-file "/home/mahlet/webCodes/moses_result.scm")
				"""
		scheme_eval(atomspace,scheme_clear)
		scheme_eval(atomspace,scheme_code)

		#start the REST API
		IP_ADDRESS = '0.0.0.0'
		PORT = 5000
		api = RESTAPI(atomspace)
		api.run(host=IP_ADDRESS, port=PORT)
