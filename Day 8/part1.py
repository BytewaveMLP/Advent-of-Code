import sys
import os

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	data = f.read()

width = 25
height = 6

layers = {}

for layer_num in range(0, len(data) // (width*height)):
	layer = []
	counts = [0, 0, 0]
	for row in range(0, height):
		for col in range(0, width):
			pixel = int(data[layer_num * (width*height) + (row*width) + col])
			counts[pixel] += 1
	
	layers[layer_num] = counts

min_zeroes = min(layers.values(), key=lambda layer: layer[0])
print(min_zeroes[1] * min_zeroes[2])