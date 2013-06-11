
import os
import subprocess


class C_Interpreter:
	def __init__(self):
		self.cpp_name = 'c_interpreter.cpp'
		
		f = open(self.cpp_name, 'w') #clear file of previous workings
		f.close()

		self.loc = 'MAIN'
		self.prompt = '{} >>> '.format(self.loc)
		self.proc = [] #preprocessor
		self.proc_name = 'PROC'
		self.name = [] #namespaces
		self.name_name = 'NAME'
		self.func = [] #definitions of func/class
		self.func_name = 'FUNC'
		self.main = [] #main
		self.main_name = 'MAIN'
		
		
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
		main_str1 = '\nint main(){\n'
		main_str2 = '\n}\n'
		
		self.buffer = self.proc + self.name + self.func
		self.buffer.append(main_str1)
		self.buffer += self.main
		self.buffer.append(main_str2)

			
	def stripoff(self, s):
		'''strip off buffer loc command'''
		return s[4:] 
		

	def run(self):
		user = input(self.prompt)
		
		try:
			if user == 'EXEC':
				#print(self.buffer)
				self.update()
				return
			elif user == 'BUFF':
				print(self.loc)
				return
			elif user == 'HELP':
				print(self.help())
				return
			elif user == 'CLEAR':
				self.buffer = []
				self.proc = []
				self.name = []
				self.func = []
				self.main = []
				return
			elif user == 'CLEAR {}'.format(self.main_name):
				self.main = []
				return
				
			#if command and code

			elif user.split()[0] == self.main_name:
				self.loc = self.main_name
				self.main.append(self.stripoff(user) + '\n')
			elif user.split()[0] == self.func_name:
				self.loc = self.func_name
				self.func.append(self.stripoff(user) + '\n')
			elif user.split()[0] == self.name_name:
				self.loc = self.name_name
				self.name.append(self.stripoff(user) + '\n')
			elif user.split()[0] == self.proc_name:
				self.loc = self.proc_name
				self.proc.append(self.stripoff(user) + '\n')


				
			#if no command
			elif self.loc == self.main_name:
				self.main.append(user + '\n')
			elif self.loc == self.func_name:
				self.func.append(user + '\n')
			elif self.loc == self.name_name:
				self.name.append(user + '\n')
			elif self.loc == self.proc_name:
				self.proc.append(user + '\n')
		except IndexError:
			return
		
		self.prompt = '{} >>> '.format(self.loc)
		if self.loc == self.main_name: #only execvute when in main
			self.update()
			
	def help(self):
		s = ''
		s += '[{} <code>]  send if code, and change to preprocessors buffer\n'.format(self.proc_name)
		s += '[{} <code>]  send if code, and change to namespaces buffer\n'.format(self.name_name)
		s += '[{} <code>]  send if code, and change to defintion of function or class buffer\n'.format(self.func_name)
		s += '[{} <code>]  send if code, and change to defintion of main functions buffer\n'.format(self.main_name)
		s += '[<code>]       send code to current buffer\n'
		s += '[CLEAR]        clear all buffers\n'
		s += '[CLEAR {}]   clear mains buffer\n'.format(self.main_name)
		s += '[EXEC]         compile and execute regardless of current buffer\n'
		s += '[HELP]         display this help menu\n'
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

