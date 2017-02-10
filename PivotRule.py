#Pivot rule
from fractions import Fraction
import random
class PivotRule:
	def __init__(self):
		self.bounded = True


	def bland_rule(self, curr_dict, n, m):
		enter, leave = (-1, -1)
		
		poss_enter = [idx for idx in range(n+m+1) if curr_dict[-1][idx] > 0]
		if (len(poss_enter) == 0):
			return (-1, -1)
		else:
			enter = min(poss_enter)

		poss_leave = [(Fraction(-1)*curr_dict[i][-1]/curr_dict[i][enter],i) for i in range(m) if curr_dict[i][enter] < 0]
		if (len(poss_leave) == 0):
			return (enter, -1)
		else:
			return (enter,min(poss_leave)[1])

	def max_coef(self, curr_dict, n, m):
		enter, leave = (-1, -1)
		
		poss_enter = [(val,idx) for idx,val in enumerate(curr_dict[-1][:n+m+1]) if val > 0]
		if (len(poss_enter) == 0):
			return (-1, -1)

		enter = max(poss_enter)[1]

		poss_leave = [(Fraction(-1)*curr_dict[i][-1]/curr_dict[i][enter],i) for i in range(m) if curr_dict[i][enter] < 0]
		if (len(poss_leave) == 0):
			return (enter, -1)
		else:
			return (enter,min(poss_leave)[1])

	def my_rule(self, curr_dict, n, m):
		enter, leave = (-1, -1)

		poss_enter = [(val,idx) for idx,val in enumerate(curr_dict[-1][:n+m+1]) if val > 0]
		if (len(poss_enter) == 0):
			return (-1, -1)

		inc_val = []

		for tmp_e in poss_enter:
			poss_leave = [(Fraction(-1)*curr_dict[i][-1]/curr_dict[i][tmp_e[1]],i) for i in range(m) if curr_dict[i][tmp_e[1]] < 0]
			if(len(poss_leave) == 0):
				return (tmp_e[1], -1)
			tmp_l = min(poss_leave)
			inc_val.append((tmp_e[0]*tmp_l[0], tmp_e[1], tmp_l[1]))

		leave = max(inc_val)
		return (leave[1], leave[2])




