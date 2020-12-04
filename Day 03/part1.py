import sys

with open(sys.argv[1], 'r') as f:
	wires = [[turn.strip() for turn in wire.split(',')] for wire in f.readlines()]

wire_points = [set(), set()]

for n, wire in enumerate(wires):
	x = 0
	y = 0
	for turn in wire:
		for i in range(0, int(turn[1:])):
			wire_points[n].add((x, y))
			if turn[0] == 'R':
				x += 1
			elif turn[0] == 'L':
				x -= 1
			elif turn[0] == 'U':
				y += 1
			elif turn[0] == 'D':
				y -= 1

intersection = sorted(wire_points[0] & wire_points[1], key=lambda pt: pt[0] + pt[1])

print(intersection)