import numpy as np
def taup_invert(p,v):
	''' This program make a G matrix for taup inverstion
	h is array of thickness (km)
	j is the number of layers
	p is the ray parameter for each layer
	
	G[ij] = 2*(u(i)**2-p(j)**2)**1/2
	'''
	v = np.array(v)
	j = len(p)
	matrix = []
	u = 1/v
	for row in range(0,j-1):
		for i in range(0, row + 1):
			G = 2*(u[i]**2-p[row+1]**2)**(1./2)
			matrix.append(G)
		for null in range(0,j-2-row):
			matrix.append(0)
	matrix = np.matrix(matrix)
	GM = matrix.reshape(j-1,j-1)
	return GM

def solve_h(taupM, GM):
	'''Solve for h using least square method'''
	h = np.linalg.inv(GM.T.dot(GM)).dot(GM.T).dot(taupM)
	return h
