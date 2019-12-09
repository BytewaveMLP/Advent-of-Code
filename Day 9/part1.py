import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from intcode import Intcode

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	data = f.read().split(',')

ic = Intcode([int(n) for n in data])
ic.input.append(1)
ic.run_until_complete()
print(ic.output)