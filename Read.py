import sys
from fractions import Fraction


def read_line(file):
	temp = file.readline().rstrip().split(' ')
	return temp


def read_input_file(args):
	try:
		f = open(args.file)
	except:
		print("Wrong input file")
		sys.exit(0)

	n, m, c, b, A = (-1, -1, [], [], [])
	try:
		n = int(f.readline())
		m = int(f.readline())

		# read vectors c, and b
		for val in read_line(f):
			tmp = val.split('/')
			c.append(Fraction(int(tmp[0]), int(tmp[1]) if len(tmp) > 1 else 1))

		for val in read_line(f):
			tmp = val.split('/')
			b.append(Fraction(int(tmp[0]), int(tmp[1]) if len(tmp) > 1 else 1))

		# read matrix
		for idx in range(m):
			row = []
			for val in read_line(f):
				tmp = val.split('/')
				row.append(Fraction(int(tmp[0]), int(tmp[1]) if len(tmp) > 1 else 1))
			A.append(row)
		# read everything

		return n, m, A, b, c
	except Exception as e:
		print("Wrong file format")
		print(str(e))
		sys.exit(0)
