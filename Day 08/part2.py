import sys
import os

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	data = f.read()

width = 25
height = 6

image = [[2] * width for _ in range(height)]

pixels = iter(data)
for layer_num in range(0, len(data) // (width*height)):
	for row in range(0, height):
		for col in range(0, width):
			pixel = int(next(pixels))
			if image[row][col] == 2 and pixel != 2:
				image[row][col] = pixel

print('\n'.join([''.join(['+' if px == 1 else ' ' for px in row]) for row in image]))