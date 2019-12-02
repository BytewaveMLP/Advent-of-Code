import sys
import os

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	mem = list(map(int, f.readline().split(',')))

mem[1] = 12
mem[2] = 2

print(','.join(str(x) for x in mem))

for pc in range(0, len(mem), 4):
	i_str = ','.join(str(x) for x in mem[pc:pc+4])
	orig_dest = mem[pc+3]
	if mem[pc] == 99:
		break
	elif mem[pc] == 1:
		mem[mem[pc+3]] = mem[mem[pc+1]] + mem[mem[pc+2]]
	elif mem[pc] == 2:
		mem[mem[pc+3]] = mem[mem[pc+1]] * mem[mem[pc+2]]
	print(f'PC = {pc}, I = {i_str}, X = {mem[mem[pc+1]]}, Y = {mem[mem[pc+2]]}, R = {mem[orig_dest]}')

print(','.join(str(x) for x in mem))

