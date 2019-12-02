import math
import functools
import operator
import sys
import os

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

def fuel_for_mass(mass):
	return math.floor(mass / 3) - 2

with open(sys.argv[1], 'r') as f:
	masses = f.readlines()

print(functools.reduce(operator.add, map(lambda mass: fuel_for_mass(int(mass)), masses)))