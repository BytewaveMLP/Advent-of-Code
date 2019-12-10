import sys
import os
import math

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	field = [line.strip() for line in f.readlines()]

observable_asteroids = {}

for i, row in enumerate(field):
	for j, space in enumerate(row):
		if space == '.': continue
		observable_asteroids[(j, i)] = set()
		for i2, row2 in enumerate(field):
			for j2, space2 in enumerate(row2):
				if space2 == '.': continue
				if i2 == i and j2 == j: continue
				gcd = math.gcd(i2-i, j2-j)
				observable_asteroids[(j, i)].add(((i2-i)//gcd, (j2-j)//gcd))

best_pos = max(observable_asteroids, key=lambda k: len(observable_asteroids[k]))
print(best_pos, len(observable_asteroids[best_pos]))