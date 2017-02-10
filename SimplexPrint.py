from enum import Enum


def print_dict(simplex_object):
	print("*************************************")
	for idx, row in enumerate(simplex_object.d):
		if idx != simplex_object.m:
			print("x_%d = " % (simplex_object.basic_var[idx]), end='')
		else:
			print("------------------------------------------")
			print("z = ", end='')
		for jdx ,val in enumerate(row):
			if jdx == len(row)-1:
				print("%s" % str(val) if val < 0 else " + " + str(val))
			else:
				if val:
					print("%sx_%d" % (str(val) if val < 0 else ' + ' + str(val), jdx), end=' ')


def print_final_status(simplex_object):
	print("OUTPUT")
	user_friendly_result = {SimplexStatus.INFEASIBLE: "infeasible",
							SimplexStatus.FEASIBLE_UNBOUNDED: "feasible but unbounded",
							SimplexStatus.FEASIBLE: "feasible but optimal solution is not found",
							SimplexStatus.OPTIMAL: "optimal"}

	print("The given LP is %s" % user_friendly_result[simplex_object.status])
	if simplex_object.status == SimplexStatus.OPTIMAL:
		print("The maximum value of objective function is: %s" % str(simplex_object.d[-1][-1]))
		print("One optimal solution is: ", end='')
		for var in range(1, simplex_object.n + 1):
			if var in simplex_object.basic_var:
				print("x_%d = %s," % (var, simplex_object.d[simplex_object.basic_var.index(var)][-1]), end='')
			else:
				print("x_%d = 0," % var, end='')

	print("\nNumber of iterations (phase1 not included): %d" % simplex_object.iter_num)
	print("Pivot rule: %s" % simplex_object.str_pivot_rule)


class SimplexStatus(Enum):
	INFEASIBLE = 1
	FEASIBLE_UNBOUNDED = 2
	FEASIBLE_BOUNDED = 3
	FEASIBLE = 4
	OPTIMAL = 5
	UNKNOWN = -1