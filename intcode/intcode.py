class Intcode():
	def get_arg(self, n, mode):
		addr = self.tape[self.pc + n]

		if mode == 1: return addr
		elif mode == 0: return self.tape[addr]
		else:
			raise ValueError(f'Argument mode {mode} not implemented')
	
	@property
	def running(self):
		return self.pc < len(self.tape)

	def __init__(self, tape):
		self.tape = tape
		self.instructions = {}
		self.instructions[99] = lambda i, _: len(self.tape)
		self.pc = 0
	
	def add_inst(self, code, fn):
		if code in self.instructions.keys():
			raise ValueError(f'Instruction already defined for code {code}')
		self.instructions[code] = fn
	
	def step(self):
		if not self.running: return False

		inst_raw = self.tape[self.pc]
		inst = inst_raw % 100
		addr_modes = [(inst_raw // n) % 10 for n in [100, 1000, 10000]]
		self.pc = self.instructions[inst](self, addr_modes)

		return True
	
	def run_until_complete(self):
		while self.step():
			pass
