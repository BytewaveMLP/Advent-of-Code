class Intcode():
	def __init__(self, tape):
		self.tape = tape
		self.input = []
		self.output = []
		self.addr_modes = []
		self.pc = 0

	@property
	def running(self):
		return self.pc < len(self.tape)
	
	def get_arg(self, n):
		addr = self.tape[self.pc + n]
		mode = self.addr_modes[n - 1]

		if mode == 1: return addr
		elif mode == 0: return self.tape[addr]
		else:
			raise ValueError(f'Argument mode {mode} not implemented')
	
	def step(self):
		if not self.running: return False

		inst_raw = self.tape[self.pc]
		inst = inst_raw % 100
		self.addr_modes = [(inst_raw // n) % 10 for n in [100, 1000, 10000]]

		getattr(self, f'intcode_inst_{inst}', self.intcode_inst_not_found)()

		return True
	
	def run_until_complete(self):
		while self.step():
			pass

	def intcode_inst_1(self):
		"""
		add a, b, dest
		"""

		self.tape[self.tape[self.pc+3]] = self.get_arg(1) + self.get_arg(2)
		self.pc += 4

	def intcode_inst_2(self):
		"""
		mul a, b, dest
		"""

		self.tape[self.tape[self.pc+3]] = self.get_arg(1) * self.get_arg(2)
		self.pc += 4

	def intcode_inst_3(self):
		"""
		in  dest
		"""

		if len(self.input) == 0: return
		self.tape[self.tape[self.pc+1]] = self.input.pop(0)
		self.pc += 2

	def intcode_inst_4(self):
		"""
		out a
		"""

		self.output.append(self.tape[self.tape[self.pc+1]])
		self.pc += 2

	def intcode_inst_5(self):
		"""
		jgz val, addr
		"""

		if self.get_arg(1) != 0:
			self.pc = self.get_arg(2)
		else:
			self.pc += 3

	def intcode_inst_6(self):
		"""
		jez val, addr
		"""

		if self.get_arg(1) == 0:
			self.pc = self.get_arg(2)
		else:
			self.pc += 3

	def intcode_inst_7(self):
		"""
		lt  a, b, dest
		"""

		self.tape[self.tape[self.pc+3]] = 0
		if self.get_arg(1) < self.get_arg(2):
			self.tape[self.tape[self.pc+3]] = 1
		self.pc += 4

	def intcode_inst_8(self):
		"""
		eq  a, b, dest
		"""

		self.tape[self.tape[self.pc+3]] = 0
		if self.get_arg(1) == self.get_arg(2):
			self.tape[self.tape[self.pc+3]] = 1
		self.pc += 4
	
	def intcode_inst_99(self):
		"""
		hlt
		"""

		self.pc = len(self.tape)

	def intcode_inst_not_found(self):
		raise ValueError(f'Instruction {self.tape[self.pc]} not found at pc={self.pc}')