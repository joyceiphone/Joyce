import numpy as np
import operator
import math
from collections import Counter

class logisticRegression(object):
	def __init__(self, filename):
		self.filename = filename
		self.X, self.y = self.fileToMatrix()

	def fileToMatrix(self):
		data = np.loadtxt(self.filename)
		X = np.c_[np.ones((data.shape[0], 1)),data[:,:-1]]
		y = data[:, -1]

		return np.mat(X), np.mat(y)
	
	def sigmoid(self, inX):
		return 1/(1 + np.exp(-inX))

	def Grad_descent(self):
		iteration = 1000
		alpha = 0.001

		n = self.X.shape[1]

		weights = np.ones((n, 1))

		for i in range(iteration):
			z = self.X*weights
			y_hat = self.sigmoid(z)

			diff = y_hat - self.y.transpose()
			X_ = self.X.transpose()
			weights = weights - alpha*X_*diff

		return weights

	def run(self):
		print(self.Grad_descent())

if __name__ == "__main__":
	obj = logisticRegression('testSet.txt')
	obj.run()
