import sys
import os
import itertools

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

# Password:
#   - 6 digit number
#   - **ONLY** 2 adjacent digits are the same
#   - Never decreases LTR, always same or increases

with open(sys.argv[1], 'r') as f:
	pwd_range_raw = [int(n) for n in f.readline().split('-')]
	pwd_range = range(pwd_range_raw[0], pwd_range_raw[1]+1)

def sort_digits(n):
	return int("".join(sorted(str(n))))

def adj_pair_eq(n):
	pairs_map = {}
	str_n = str(n)
	for i in range(len(str_n) - 1):
		a, b = str_n[i], str_n[i+1]

		if a == b:
			if a not in pairs_map:
				pairs_map[a] = 2
			else:
				pairs_map[a] += 1
	
	for n in pairs_map:
		if pairs_map[n] == 2: return True
	
	return False

print(len([n for n in pwd_range if sort_digits(n) == n and adj_pair_eq(n)]))