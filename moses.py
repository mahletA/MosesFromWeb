from opencog.pymoses import moses
class mses:
	def __init__(self, put):
		self.args = put
		self.moses=moses()
		input_data=[[0,0,0],[0,1,0],[1,0,0],[1,1,1]]
		self.output=self.moses.run(input=input_data,args=self.args,Scheme=True)
		#print output[3].program
	def getres(self):
		return self.output

