import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from intcode import Intcode
from copy import deepcopy
import itertools

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	mem = list(map(int, f.readline().split(',')))

amplifiers = [Intcode(mem.copy()) for i in range(0, 5)]

phase_settings = range(5, 10)
phase_setting_arrangements = itertools.permutations(phase_settings, 5)

max_output_signals = []

for settings in phase_setting_arrangements:
	for i, amp in enumerate(amplifiers):
		amp.pc = 0
		amp.tape = mem.copy()
		amp.input.append(settings[i])
		amp.step() # consume first input value
	amplifiers[0].input.append(0)

	while amplifiers[-1].running:
		for i, amp in enumerate(amplifiers):
			while True:
				old_pc = amp.pc
				amp.step()
				if old_pc == amp.pc:
					break
			amplifiers[(i + 1) % len(amplifiers)].input.append(amp.output.pop())
	max_output_signals.append(amplifiers[0].input.pop())

print(max(max_output_signals))