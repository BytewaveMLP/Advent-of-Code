import sys
import os

if len(sys.argv) < 3:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt> <target>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	orig_mem = list(map(int, f.readline().split(',')))

for noun in range(0, 100):
	for verb in range(0, 100):
		mem = orig_mem.copy()
		mem[1] = noun
		mem[2] = verb
		for pc in range(0, len(mem), 4):
			i_str = ','.join(str(x) for x in mem[pc:pc+4])
			orig_dest = mem[pc+3]
			if mem[pc] == 99:
				break
			elif mem[pc] == 1:
				mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
			elif mem[pc] == 2:
				mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
		
		if mem[0] == int(sys.argv[2]):
			print(noun * 100 + verb)
			exit(0)
