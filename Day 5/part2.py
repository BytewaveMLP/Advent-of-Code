import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from intcode import Intcode

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	mem = list(map(int, f.readline().split(',')))

# mem[1] = 12
# mem[2] = 2

intcode = Intcode(mem)

def intcode_inst_add(i, addr_modes):
	i.tape[i.tape[i.pc+3]] = i.get_arg(1, addr_modes[0]) + i.get_arg(2, addr_modes[1])
	return i.pc + 4

def intcode_inst_mul(i, addr_modes):
	i.tape[i.tape[i.pc+3]] = i.get_arg(1, addr_modes[0]) * i.get_arg(2, addr_modes[1])
	return i.pc + 4

def intcode_inst_in(i, addr_modes):
	i.tape[i.tape[i.pc+1]] = int(input('INPUT: '))
	return i.pc + 2

def intcode_inst_out(i, addr_modes):
	print(i.tape[i.tape[i.pc+1]])
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

intcode.add_inst(1, intcode_inst_add)
intcode.add_inst(2, intcode_inst_mul)
intcode.add_inst(3, intcode_inst_in)
intcode.add_inst(4, intcode_inst_out)
intcode.add_inst(5, intcode_inst_jt)
intcode.add_inst(6, intcode_inst_jf)
intcode.add_inst(7, intcode_inst_lt)
intcode.add_inst(8, intcode_inst_eq)

# print(','.join(str(x) for x in intcode.tape))

intcode.run_until_complete()

# print(','.join(str(x) for x in intcode.tape))
