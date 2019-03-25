import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
from sympy import isprime as is_prime

class Spiral_Display():

	def __init__(self, cols = 9):
		self.cols = cols
		self.matrix = np.zeros((cols,cols))
		self.ptr = [round(cols/2), round(cols/2)]
		self.entrie = 1

	def append_point(self, ptr, mov, num, direction, relation):
		for i in range(mov):
			if(relation(self.entrie)):
				try:
					self.matrix[ptr[0], ptr[1]] = 1
				except IndexError:
					continue
			
			self.entrie += 1
			ptr[direction] += num 
			 
	def set_point(self, mov, relation = is_prime):
		
		if(mov % 2 == 0):
			self.append_point(self.ptr, mov, -1, 1, relation)
			self.append_point(self.ptr, mov, +1, 0, relation)

		elif(mov % 2 != 0):
			self.append_point(self.ptr, mov, +1, 1, relation)
			self.append_point(self.ptr, mov, -1, 0, relation)

	def fixed_display(self):
		print(self.matrix[1:,1:])

	def normal_display(self):
		print('\n', self.matrix)

def main():
	 M = Spiral_Display(300)

	 for i in range(M.cols)[1:]:
	 	#M.set_point(i, lambda x: x % 5 == 0)
	 	M.set_point(i)

	 M.fixed_display()
	 M.normal_display()

	 sns.heatmap(M.matrix[1:, 1:], cmap='magma',yticklabels= False, 
	 						xticklabels = False, cbar = False)
	 
	 #plt.show()
	 plt.savefig(f'figures/{M.cols}Spiral.png', dpi= 128)

if __name__ == '__main__':
	main()
