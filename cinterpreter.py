
import os
import subprocess


class C_Interpreter:
	def __init__(self):
		self.cpp_name = 'c_interpreter.cpp'
		
		f = open(self.cpp_name, 'w') #clear file of previous workings
		f.write('')
		f.close()
		
		self.prompt = '>>> '
		
		self.loc = 'MAIN'
		self.proc = [] #preprocessor
		self.name = [] #namespaces
		self.func = [] #definitions of func/class
		self.main = [] #main
		
		
		self.buffer = []
		
		self.compile = 'g++ {} -o main'.format(self.cpp_name)
		self.execute = './main'


	def write_cpp(self, buff):
		src_dir = os.path.dirname(os.path.realpath(__file__)) #dir of this file
		os.chdir(src_dir)
		f = open(self.cpp_name,'w')
		f.write(buff)
		f.close()
		
	def compile_cpp(self):
		proc = subprocess.Popen(self.compile.split())
		proc.wait()
		
	def execute_cpp(self):
		proc = subprocess.Popen(self.execute.split())
		proc.wait()
		
	def update(self):
		self.join_buffers()
		try:
			self.write_cpp(''.join(self.buffer))
			self.compile_cpp()
			self.execute_cpp()
		except FileNotFoundError:
			pass
			
	def join_buffers(self):
		main_str1 = 'int main(){\n'
		main_str2 = '}\n'
		
		self.buffer = self.proc + self.name + self.func
		self.buffer.append(main_str1)
		self.buffer += self.main
		self.buffer.append(main_str2)

			
	def stripoff(self, s):
		'''strip off buffer loc command'''
		return s[4:] + '\n'
		

	def run(self):
		user = input(self.prompt)
		
		
		if user == 'EXEC':
			#print(self.buffer)
			self.update()
		elif user == 'BUFF':
			print(self.loc)
		elif user == 'HELP':
			print(self.help())
		elif user == 'CLEAR':
			self.buffer = []
			
		elif user.split()[0] == 'MAIN':
			self.loc = 'MAIN'
			self.main.append(self.stripoff(user))
		elif user.split()[0] == 'FUNC':
			self.loc = 'FUNC'
			self.func.append(self.stripoff(user))
		elif user.split()[0] == 'NAME':
			self.loc = 'NAME'
			self.name.append(self.stripoff(user))
		elif user.split()[0] == 'PROC':
			self.loc = 'PROC'
			self.proc.append(self.stripoff(user))
			
		elif self.loc == 'MAIN':
			self.main.append(user)
		elif self.loc == 'FUNC':
			self.func.append(user)
		elif self.loc == 'NAME':
			self.name.append(user)
		elif self.loc == 'PROC':
			self.proc.append(user)
			
	def help(self):
		s = '''PROC <code> prefix code with command or just command to change to preprocessor's buffer

NAME <code> prefix code with command or just command to change to namespace's buffer

FUNC <code> prefix code with command or just command to change to defintion of function or class' buffer

MAIN <code> prefix code with command or just command to change to main function's buffer (int main(){} is already created)
		'''
		return s
		
		'''
		print('location is: {}'.format(self.loc))
		print(self.proc)
		print(self.name)
		print(self.func)
		print(self.main)
		'''
		#print('location is: {}'.format(self.loc))

		'''
		else:
			self.buffer.append(user + '\n')
		print(self.buffer)
		'''

app = C_Interpreter()

while True:
	try:
		app.run()
	except KeyboardInterrupt:
		print('\n')
		break

