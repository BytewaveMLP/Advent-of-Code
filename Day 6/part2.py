import sys
import os

class OrbitingBody():
	def __init__(self, name):
		self.name = name
		self.parent = None
		self.children = []
	
	def set_parent(self, parent):
		self.parent = parent
	
	def add_child(self, child):
		self.children.append(child)
	
	def __repr__(self):
		return self.name

def common_ancestor(body1, body2):
	ancestors_visited = {}

	n = 0

	while body1 != None:
		ancestors_visited[body1] = n
		n += 1
		body1 = body1.parent
	
	while body2 != None:
		if body2 in ancestors_visited.keys():
			return ancestors_visited[body2]
		body2 = body2.parent
	
	return None

if len(sys.argv) < 2:
	print(f'usage: {os.path.basename(sys.argv[1])} <input.txt>')
	exit(1)

with open(sys.argv[1], 'r') as f:
	orbits = f.readlines()

orbiting_bodies = {}

for orbit in orbits:
	bodies = [body.strip() for body in orbit.split(')')]
	if bodies[0] not in orbiting_bodies.keys():
		orbiting_bodies[bodies[0]] = OrbitingBody(bodies[0])
	if bodies[1] not in orbiting_bodies.keys():
		orbiting_bodies[bodies[1]] = OrbitingBody(bodies[1])
	
	orbiting_bodies[bodies[1]].set_parent(orbiting_bodies[bodies[0]])
	orbiting_bodies[bodies[0]].add_child(orbiting_bodies[bodies[1]])

YOU = orbiting_bodies['YOU']
SAN = orbiting_bodies['SAN']

print(common_ancestor(YOU, SAN) + common_ancestor(SAN, YOU) - 2)