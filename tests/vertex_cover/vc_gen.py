#vertex cover generator:

import sys
import random


class Graph:
	def __init__(self, n):
		self.n = n
		self.edges = []

	def add_edge(self, u, v):
		self.edges.append((u,v))

def main():
	n = int(sys.argv[1])
	#size of the graph
	g = Graph(n)
	for i in range(n):
		for j in range(i+1,n):
			p = random.randrange(0,2)
			if p == 1:
				g.add_edge(i,j)

	m = len(g.edges)
	c = [-1]*n
	b = [-1]*m + [1]*n
	A = []
	for e in g.edges:
		row = [0 for i in range(n)]
		print(e)
		row[e[0]] = -1
		row[e[1]] = -1
		A.append(row)

	
	for i in range(n):
		row = [0 for i in range(n)]
		row[i] = 1
		A.append(row)

	f = open("graph.out", "w")
	f.write("%d\n" % n)
	f.write("%d\n" % m)
	for e in g.edges:
		f.write("%d %d\n"%(e[0],e[1]))

	f.close()

	f = open("vc_graph.dat", "w")
	f.write("%d\n" %n)
	f.write("%d\n" %len(b))

	for el in c:
		f.write("%d " % el)
	f.write('\n')

	for el in b:
		f.write("%d " % el)
	f.write('\n')

	for row in A:
		for el in row:
			f.write("%d " % el)
		f.write('\n')

	f.close()

if __name__ == '__main__':
	main()