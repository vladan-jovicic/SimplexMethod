from fractions import Fraction
from PivotRule import *

from SimplexPrint import *


class Simplex:
	def __init__(self, A, b, c, m, n, verbose=False, piv_rule="blands", max_iter=-1):
		# define variables
		self.A, self.b, self.c = (A, b, c)
		self.d = []
		self.n, self.m = (n, m)
		self.iter_num = 0
		self.max_iter = max_iter
		self.str_pivot_rule = piv_rule
		self.pivotRule = {"blands": PivotRule().bland_rule, "max_coef": PivotRule().max_coef, "my_rule": PivotRule().my_rule}[piv_rule]
		self.status = SimplexStatus.UNKNOWN
		self.verbose = verbose
		self.basic_var = [i for i in range(n+1, self.n+self.m+1)]

		# initial dictionary
		for i in range(self.m):
			self.d.append([Fraction(0)] + [Fraction(-1)* x for x in self.A[i]] + [0 for i in range(self.m)] + [b[i]])
		self.d.append([0] + self.c + [0 for i in range(self.m + 1)])

		if self.verbose:
			print("The initial dictionary is")
			self.print_dict()
	
	def get_status(self):
		return self.status

	def solve(self):
		while self.status not in [SimplexStatus.OPTIMAL, SimplexStatus.INFEASIBLE, SimplexStatus.FEASIBLE_UNBOUNDED]:
			if self.max_iter != -1 and self.iter_num >= self.max_iter:
				# maximum number of iteration reached
				return self.status
			self.iterate_one_step()
		return self.status

	def phase1(self):
		"""This is the phase1 of the simplex method.
		If the zero is unfeasible, it finds a basic feasible solution or
		states that the program is infeasible.
		If a basic feasible solution is found, the dictionary corresponding to it is constructed
		"""
		if self.verbose:
			print("Entering phase 1")

		for j in range(self.m):
			self.d[j][0] = 1
		for j in range(self.n + self.m + 2):
			self.d[-1][j] = 0
		self.d[-1][0] = -1

		# find the most defected value
		# so called illegal pivot rule
		mini, idx = min((mini, idx) for idx,mini in enumerate(self.b))
		self.apply_pivot(0, idx)
		if self.verbose:
			self.print_dict()

		while True:
			enter, leave = self.pivotRule(self.d, self.n, self.m)
			if enter != -1:
				self.apply_pivot(enter, leave)
				if self.verbose:
					self.print_dict()
				continue

			# the simplex can not proceed anymore
			if self.d[self.m][-1] != 0:
				self.status = SimplexStatus.INFEASIBLE
				return self.status
		
			if self.verbose:
				print("A basic feasible solution found")

			# the case when x_0 is in basis
			if 0 in self.basic_var:
				idx = self.basic_var.index(0)
				enter = min([idx for idx, val in enumerate(self.d[idx]) if idx < self.n + self.m + 1 and val > 0])
				self.apply_pivot(enter, idx)

			for j in range(self.m+1):
				self.d[j][0] = 0
			
			for var in range(1, self.n + 1):
				try:
					idx = self.basic_var.index(var)
					for i in range(1,self.n + self.m + 2):
						self.d[-1][i] += self.c[var-1]*self.d[idx][i]
				except:
					self.d[-1][var] += self.c[var-1]

			if self.verbose:
				self.print_dict()
			
			self.status = SimplexStatus.FEASIBLE
			return self.status

	def iterate_one_step(self):
		if self.status not in [SimplexStatus.FEASIBLE, SimplexStatus.UNKNOWN]:
			return self.status

		if self.iter_num == 0:
			if min(self.b) < 0:
				if self.phase1() == SimplexStatus.INFEASIBLE:
					return self.status

		enter, leave = self.pivotRule(self.d, self.n, self.m)

		if enter == -1:
			self.status = SimplexStatus.OPTIMAL
		elif enter > 0 and leave == -1:
			self.status = SimplexStatus.FEASIBLE_UNBOUNDED
		else:
			self.apply_pivot(enter, leave)
			if self.verbose:
				self.print_dict()
			self.iter_num += 1
		
		return self.status

	def apply_pivot(self, enter, leave):
		if self.verbose:
			print("Entering %d, leaving %d" %(enter, self.basic_var[leave]))

		# solve for x_enter
		divider = Fraction(-1)*self.d[leave][enter]
		self.d[leave][self.basic_var[leave]] = -1
		self.basic_var[leave] = enter
		for i in range(self.n+self.m+2):
			self.d[leave][i] /= divider
			self.d[leave][i] = 0 if i == enter else self.d[leave][i]

		for i in range(self.m+1):
			if i == leave:
				continue
			multiplier = self.d[i][enter]
			self.d[i][enter] = 0
			for j in range(self.n + self.m + 2):
				self.d[i][j] += multiplier*self.d[leave][j]

	def print_dict(self):
		print_dict(self)

	def print_final_status(self):
		print_final_status(self)

