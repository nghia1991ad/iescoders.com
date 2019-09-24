from ttcal import layerxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

v_model = pd.read_csv('v_model.dat')

p1 = 0.1236
p2 = 0.2217
n = 100

result = [['p','X','T']]
for p in np.linspace(p1, p2, n):
	X = 0; T = 0;
	for i in range(0, len(v_model)-1):
        	p = p
        	h = v_model.h[i+1] - v_model.h[i]
        	utop = 1/v_model.vp[i]
        	ubot = 1/v_model.vp[i+1]
        	dx, dt, irtr = layerxt(p,h,utop,ubot)
        	X += dx; T += dt
		#If the ray reflected at layer the dx, dt calculation stops
        	if irtr == 2:
                	break
        result.append([p,X,T])

result_df = pd.DataFrame(result, columns=result.pop(0))
result_df = result_df[::-1]

#Multiply by 2 to get total surface-to-surface value ot X(p) and T(p)
result_df['T'] = 2*result_df['T']
result_df['X'] = 2*result_df['X']

plt.figure(1)
result_df['RT'] = result_df['T']-result_df['X']/8
result_df.plot(x='X', y='RT', legend=False)
plt.title('Reduction time')
plt.ylabel('Reduce time T - X/8 (s)')
plt.xlabel('Distance (km)')
plt.text(20,0.80,'Prograde', rotation =40)
plt.text(40,1.6,'Retrograde', rotation =35)
plt.text(80,1.00,'Prograde', rotation =0)
plt.savefig('ex4.8.1.png')

plt.figure(2)
result_df.plot(x='p', y='X', legend=False)
plt.title('X(p)')
plt.ylabel('Distance X (km)')
plt.xlabel('Ray parameter (km/s)')
plt.xlim([p1,p2])
plt.savefig('ex4.8.2.png')

plt.figure(3)
result_df['Taup'] = result_df['T'] - result_df['p']*result_df['X']
result_df.plot(x='p', y='Taup', legend=False)
plt.title('Tau(p)')
plt.ylabel('Tau(p) (s)')
plt.xlabel('Ray parameter (km/s)')
plt.xlim([p1,p2])
plt.savefig('ex4.8.3.png')

plt.figure(4)
v_model.h = v_model.h * (-1)
v_model.plot(x='vp', y='h', legend=False)
plt.ylabel('Depth (km)')
plt.xlabel('Velocity (km/s)')
plt.xlim([4,9])
plt.ylim([-10,0])
plt.savefig('ex4.8.4.png')

#plt.show()


