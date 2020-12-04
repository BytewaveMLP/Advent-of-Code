import sys
import os
import itertools

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

# Password:
#   - 6 digit number
#   - 2 adjacent digits are the same
#   - Never decreases LTR, always same or increases

with open(sys.argv[1], 'r') as f:
	pwd_range_raw = [int(n) for n in f.readline().split('-')]
	pwd_range = range(pwd_range_raw[0], pwd_range_raw[1]+1)

def sort_digits(n):
	return int("".join(sorted(str(n))))

def pairwise(iterable):
	"s -> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = itertools.tee(iterable)
	next(b, None)
	return zip(a, b)

def adj_pair_eq(n):
	for a, b in pairwise(str(n)):
		if a == b: return True
	
	return False

print(len(list(filter(lambda n: sort_digits(n) == n and adj_pair_eq(n), pwd_range))))