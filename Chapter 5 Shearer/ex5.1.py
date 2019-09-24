import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from taup_invert import taup_invert, solve_h

def fit_line(tx, seg_top, seg_bot):
	p_rs = []; tau_rs = []	
	for i in range(0, len(seg_top)):	
		X = tx['X'][(tx['X']>seg_top[i]) & (tx['X'] <seg_bot[i])]
		T = tx['T'][(tx['X']>seg_top[i]) & (tx['X'] <seg_bot[i])]
		if i == 0:
			X = np.array(X)
			X = X[:,np.newaxis]
			p, _, _, _ = np.linalg.lstsq(X,T)
			p = p.tolist()
			p = p[0]
			tau = 0
			p_rs.append(p); tau_rs.append(tau)
		else:
			p,tau = np.polyfit(X,T,1)
			p_rs.append(p); tau_rs.append(tau)
	return p_rs, tau_rs
def plot_fit(p, tau, seg_top, seg_bot):
	for i in range(0,len(p)):
		x = np.linspace(seg_top[i], seg_bot[i], 100)
		t = p[i]*x + tau[i]
		plt.plot(x,t)

tx = pd.read_csv('TXpoints.txt',sep='\s+')


#Plot the new T-X
plt.figure(1)
plt.plot(tx['X'],tx['T'],'.')
plt.title('TX plot')
plt.ylabel('T (s)')
plt.xlabel('X (km)')
plt.grid(b=True, which='both', color='0.65',linestyle='-')

#Create segments of lines
seg_top = [   0, 20,  50, 100, 150, 200]
seg_bot = [  20, 50, 100, 150, 200, 250]

#Linear fit 
p, tau = fit_line(tx, seg_top, seg_bot)

#Plot the linear fit
plot_fit(p, tau, seg_top, seg_bot)
plt.savefig('ex5.1fit.png')


#Solve for the thickness of velocity model
#Input parameters matrix: p, tau
p = p
v = 1/np.array(p) #Velocity model
GM = taup_invert(p,v) #Create GM matrix
taupM = np.matrix(tau[1:]).reshape(len(p)-1,1)
h = solve_h(taupM,GM)
#Convert matrix to a simple list
h = h.ravel().tolist()[0]

m_h = []; m_v = []
#Create a velocity model)
for i in range(0, len(v)):	
	if i == 0:
		htemp = 0; vtemp = v[i]
		m_h.append(htemp); m_v.append(vtemp)
		htemp = htemp + h[i]; vtemp = v[i]
		m_h.append(htemp); m_v.append(vtemp)
	elif i 	== len(v) - 1:
		htemp = htemp; vtemp = v[i]
		m_h.append(htemp); m_v.append(vtemp)
		htemp = htemp + 20; vtemp = v[i]
		m_h.append(htemp); m_v.append(vtemp)
	else:	
		htemp = htemp; vtemp = v[i]
		m_h.append(htemp); m_v.append(vtemp)
		htemp = htemp + h[i]; vtemp = v[i]
		m_h.append(htemp); m_v.append(vtemp)

v_model = pd.DataFrame(zip(m_h, m_v), columns = ['H','Vp'])
plt.figure(2)
plt.plot(v_model['Vp'],v_model['H'])
plt.xlim([0,10])
plt.ylim([70,0])
plt.title('Velocity model')
plt.ylabel('Depth (km)')
plt.xlabel('Velocity (km/s)')
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.savefig('ex5.1v_model.png')


