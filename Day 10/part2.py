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
		observable_asteroids[(j, i)] = {}
		for i2, row2 in enumerate(field):
			for j2, space2 in enumerate(row2):
				if space2 == '.': continue
				if i2 == i and j2 == j: continue
				gcd = math.gcd(i2-i, j2-j)
				slope = ((i2-i)//gcd, (j2-j)//gcd)
				if slope not in observable_asteroids[(j, i)].keys():
					observable_asteroids[(j, i)][slope] = []
				observable_asteroids[(j, i)][slope].append((j2, i2))
		for slope in observable_asteroids[(j, i)]:
			observable_asteroids[(j, i)][slope].sort(key=lambda pt: math.sqrt((pt[0]-j)**2 + (pt[1]-i)**2))

best_pos = max(observable_asteroids, key=lambda k: len(observable_asteroids[k]))
slopes = observable_asteroids[best_pos]

x = 0
last_destroyed = (-1, -1)

while x < 200:
	to_delete = []
	for slope in slopes:
		destroyed_one = False

		if len(slopes[slope]) > 0:
			last_destroyed = slopes[slope].pop()
			destroyed_one = True
			x += 1

		if not destroyed_one:
			to_delete.append(slope)
		
	for delete in to_delete:
		slopes.pop(delete)

print(last_destroyed[0] * 100 + last_destroyed[1])