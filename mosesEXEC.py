from os import system
import sys
from param import params
sys.path.append("/usr/local/share/moses/python/moses")
from pymoses import moses
moses=moses()
input_data=[[0,0,0],[0,1,1],[1,0,1],[1,1,0]]
output=moses.run(input=input_data ,args=params ,scheme=True)
moses.write_scheme(output)


