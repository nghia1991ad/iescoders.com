from math import sqrt, log


def layerxt(p,h,utop,ubot):
	''' LAYERXT calculates dx and dt for ray in layer with linear velocity gradient
 
	    Inputs:   p     =  horizontal slowness
             h     =  layer thickness
             utop  =  slowness at top of layer
             ubot  =  slowness at bottom of layer
	    Returns:  dx    =  range offset
             dt    =  travel time
             irtr  =  return code
                   = -1,  zero thickness layer
                   =  0,  ray turned above layer
                   =  1,  ray passed through layer
                   =  2,  ray turned within layer, 1 segment counted in dx,dt'''
# ray turned above layer
	if p >= utop:
		dx = 0
		dt = 0
		irtr = 0
		return dx,dt,irtr

#Zero thickness layer
	elif h == 0:
		dx = 0
		dt = 0
		irtr = -1
		return dx,dt,irtr

#Calculate some parameters
	u1 = utop
	u2 = ubot
	v1 = 1.0/u1
	v2 = 1.0/u2
#Slope of velocity gradient
	b = (v2 - v1)/h
	eta1 = sqrt(u1**2 - p**2)

#Constant velocity layer
	if b == 0:
		dx = h*p/eta1
		dt = h*u1**2/eta1
		irtr = 1
		return dx,dt,irtr

	x1 = eta1/(u1*b*p)
	tau1=(log((u1+eta1)/p)-eta1/u1)/b

#Ray turned within layer, no contribution to integral from bottom point
	if p >= ubot:
		dx = x1
		dtau = tau1
		dt = dtau + p*dx
		irtr = 2	
		return dx,dt,irtr

        irtr=1
	eta2=sqrt(u2**2-p**2)
	x2=eta2/(u2*b*p)
	tau2=(log((u2+eta2)/p)-eta2/u2)/b

	dx=x1-x2
	dtau=tau1-tau2

	dt=dtau+p*dx
	return dx,dt,irtr

def flat(zsph,vsph):
	''' Calculate the flatten transformation from a spherical Earth.
	    zf, vf = flat(zsph,vsph)'''
	
# Radius of the Earth
	a = 6371.0

	rsph = a - zsph
	zf = -a*log(rsph/float(a))
	vf = (a/float(rsph))*vsph
	return zf, vf
