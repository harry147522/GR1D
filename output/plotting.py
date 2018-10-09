
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

#plt.plot(r,diu[:,0])
#plt.ylabel("density (m)")
#plt.xlabel('distance from core (m)')
#plt.show()
A = np.array((100,2))
A = np.loadtxt("rhovsx.dat")

print A
plt.plot(A[:,0],A[:,1])
plt.ylabel("density (m)")
plt.xlabel('distance from core (m)')
plt.show()
