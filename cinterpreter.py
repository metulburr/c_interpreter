
import os
import subprocess


class C_Interpreter:
	def __init__(self):
		self.cpp_name = 'c_interpreter.cpp'
		
		self.prompt = '>>> '
		self.data = []
		
		self.compile = 'g++ {} -o main'.format(self.cpp_name)
		self.execute = './main'


	def write_cpp(self, data):
		src_dir = os.path.dirname(os.path.realpath(__file__)) #dir of this file
		os.chdir(src_dir)
		f = open(self.cpp_name,'w')
		f.write(data)
		f.close()
		
	def compile_cpp(self):
		proc = subprocess.Popen(self.compile.split())
		proc.wait()
		
	def execute_cpp(self):
		proc = subprocess.Popen(self.execute.split())
		proc.wait()
		
	def update(self):
		try:
			self.write_cpp(''.join(self.data))
			self.compile_cpp()
			self.execute_cpp()
		except FileNotFoundError:
			pass
		

	def run(self):
		user = input(self.prompt)
		
		
		if user == 'EXEC':
			self.update()
		elif user == 'CLEAR':
			self.data = []
		else:
			self.data.append(user + '\n')
			#print(self.data)

app = C_Interpreter()

while True:
	try:
		app.run()
	except KeyboardInterrupt:
		print('\n')
		break

