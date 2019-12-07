import sys
import os
import subprocess
import itertools

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

in_file = os.path.realpath(sys.argv[1])

intcode_interp = os.path.dirname(os.path.realpath(__file__)) + '/../Day 5/part2.py'

phase_settings = itertools.permutations(list(range(5, 10)), 5)

output_signals = []

for settings in phase_settings:
	amp_signal = 0

	for setting in settings:
		proc = subprocess.run(['python.exe', intcode_interp, in_file], input=f'{setting}\n{amp_signal}\n', capture_output=True, text=True)
		amp_signal = int(proc.stdout.split(' ')[-1])

	output_signals.append(amp_signal)

print(max(output_signals))