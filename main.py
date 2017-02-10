from fractions import Fraction
from Simplex import *
import argparse
from Read import *

def main():
	
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file", help="The input file")
	parser.add_argument("-v", "--verbose", help="Print dictionary at each iteration")
	parser.add_argument("--iter-num", help="Set the maximum number of iterations")
	parser.add_argument("-p", "--pivot", help="Select the pivot rule. One of the following values: bland, max_coef, my_rule")

	args = parser.parse_args()
	# file_name, verbose, output_file, iter_num = ("", False, None, -1)
	pivot_rule = "blands"
	
	if not args.file:
		parser.print_help()
		sys.exit(0)

	# read matrix

	n, m, A, b, c = read_input_file(args)

	if args.pivot:
		if args.pivot in ["blands", "max_coef", "my_rule"]:
			pivot_rule = args.pivot
		else:
			print("Unknown pivot! Using bland's rule instead")

	verbose = True if args.verbose else False

	iter_num = int(args.iter_num) if args.iter_num and int(args.iter_num) > 0 else -1

	# create Simplex object
	simplex = Simplex(A, b, c, m, n, verbose, pivot_rule, iter_num)

	result = simplex.solve()
	simplex.print_final_status()


if __name__ == '__main__':
	main()