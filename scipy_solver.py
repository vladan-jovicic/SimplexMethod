#this script is used for testing correctness
from scipy.optimize import linprog
from Simplex import *
from fractions import Fraction


class SimplexByScipy:
	def __init__(self, A, b, c, n, m):
		self.A = A
		self.b = b
		self.c = c
		self.res = -1
		self.n = n

	def solve(self):
		bounds = [(0,None) for i in range(self.n)]
		self.res = linprog([Fraction(-1)*x for x in self.c], A_ub = self.A, b_ub = self.b, bounds=bounds)
	
	def get_status(self):
		user_friendly = {0: SimplexStatus.OPTIMAL, 1: "limit", 
			2: SimplexStatus.INFEASIBLE, 3: SimplexStatus.FEASIBLE_UNBOUNDED}

		return user_friendly[self.res.status]
