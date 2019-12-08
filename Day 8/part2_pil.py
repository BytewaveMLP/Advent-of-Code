import sys
import os
from PIL import Image, ImageDraw

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	data = f.read()

width = 25
height = 6

image = [[2] * width for _ in range(height)]

img_out = Image.new('RGB', (width, height), (0, 0, 0))
img_out_d = ImageDraw.Draw(img_out)

pixels = iter(data)
for layer_num in range(0, len(data) // (width*height)):
	for row in range(0, height):
		for col in range(0, width):
			pixel = int(next(pixels))
			if image[row][col] == 2 and pixel != 2:
				image[row][col] = pixel
				if pixel == 1:
					img_out_d.point((col, row), fill=(255, 255, 255))

img_out.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'd8p2.png'))