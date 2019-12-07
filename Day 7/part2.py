import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from intcode import Intcode
from copy import deepcopy
import itertools

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	mem = list(map(int, f.readline().split(',')))

input_value = []
output_value = None

def intcode_inst_add(i, addr_modes):
	i.tape[i.tape[i.pc+3]] = i.get_arg(1, addr_modes[0]) + i.get_arg(2, addr_modes[1])
	return i.pc + 4

def intcode_inst_mul(i, addr_modes):
	i.tape[i.tape[i.pc+3]] = i.get_arg(1, addr_modes[0]) * i.get_arg(2, addr_modes[1])
	return i.pc + 4

def intcode_inst_in(i, addr_modes):
	global input_value
	if len(input_value) == 0: return i.pc
	i.tape[i.tape[i.pc+1]] = input_value.pop(0)
	return i.pc + 2

def intcode_inst_out(i, addr_modes):
	global output_value
	output_value = i.tape[i.tape[i.pc+1]]
	return i.pc + 2

def intcode_inst_jt(i, addr_modes):
	if i.get_arg(1, addr_modes[0]) != 0:
		return i.get_arg(2, addr_modes[1])
	return i.pc + 3

def intcode_inst_jf(i, addr_modes):
	if i.get_arg(1, addr_modes[0]) == 0:
		return i.get_arg(2, addr_modes[1])
	return i.pc + 3

def intcode_inst_lt(i, addr_modes):
	i.tape[i.tape[i.pc+3]] = 0
	if i.get_arg(1, addr_modes[0]) < i.get_arg(2, addr_modes[1]):
		i.tape[i.tape[i.pc+3]] = 1
	return i.pc + 4

def intcode_inst_eq(i, addr_modes):
	i.tape[i.tape[i.pc+3]] = 0
	if i.get_arg(1, addr_modes[0]) == i.get_arg(2, addr_modes[1]):
		i.tape[i.tape[i.pc+3]] = 1
	return i.pc + 4

amplifiers = [Intcode(mem.copy()) for i in range(0, 5)]
for amp in amplifiers:
	amp.add_inst(1, intcode_inst_add)
	amp.add_inst(2, intcode_inst_mul)
	amp.add_inst(3, intcode_inst_in)
	amp.add_inst(4, intcode_inst_out)
	amp.add_inst(5, intcode_inst_jt)
	amp.add_inst(6, intcode_inst_jf)
	amp.add_inst(7, intcode_inst_lt)
	amp.add_inst(8, intcode_inst_eq)

phase_settings = range(5, 10)
phase_setting_arrangements = itertools.permutations(phase_settings, 5)

max_output_signals = []
waiting_for_input = [False for _ in amplifiers]

for settings in phase_setting_arrangements:
	input_value = [*settings, 0]
	for amp in amplifiers:
		amp.pc = 0
		amp.tape = mem.copy()
		amp.step() # consume first input value
	while amplifiers[-1].running:
		for i, amp in enumerate(amplifiers):
			while True:
				old_pc = amp.pc
				amp.step()
				if old_pc == amp.pc:
					break
			input_value.append(output_value)
	max_output_signals.append(input_value[0])

print(max(max_output_signals))