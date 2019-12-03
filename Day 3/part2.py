import sys
import itertools

with open(sys.argv[1], 'r') as f:
	wires = [[turn.strip() for turn in wire.split(',')] for wire in f.readlines()]

wire_points = [{}, {}]

for n, wire in enumerate(wires):
	x = 0
	y = 0
	step = 0
	for turn in wire:
		for i in range(0, int(turn[1:])):
			if (x, y) not in wire_points[n]:
				wire_points[n][(x, y)] = step
			if turn[0] == 'R':
				x += 1
			elif turn[0] == 'L':
				x -= 1
			elif turn[0] == 'U':
				y += 1
			elif turn[0] == 'D':
				y -= 1
			step += 1

intersections = wire_points[0].keys() & wire_points[1].keys()

print(sorted([wire_points[0][point] + wire_points[1][point] for point in intersections]))