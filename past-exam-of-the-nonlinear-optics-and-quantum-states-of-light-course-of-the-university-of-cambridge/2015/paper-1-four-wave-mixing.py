"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Writes a literal PNG basename to cwd. No source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(2,2,figsize=(11,7),layout='constrained');a,b,c,d=axs.flat
z=np.linspace(0,1,300);q=1.;a.plot(z,np.cos(q*(1-z))/np.cos(q),label=r'$|A_3|/|a|$');a.plot(z,np.sin(q*(1-z))/np.cos(q),label=r'$|A_4|/|a|$');a.scatter([0,1],[1,0],color='black',s=18);a.set(xlabel=r'$z/L$',ylabel='Amplitude magnitude',title=r'Opposite-end boundary conditions; $\kappa L=1$');a.legend(frameon=False)
u=np.linspace(0,1.42,300);b.plot(u,np.tan(u)**2,label='Conjugate reflectivity');b.plot(u,1/np.cos(u)**2,label='Signal transmission');b.set(yscale='log',xlabel=r'$\kappa L$',ylabel='Ideal power ratio',title='Undepleted-pump gain; pole at π/2');b.legend(frameon=False)
x=np.linspace(-1,1,400);phase=.9*x*x+.5*x**3;c.plot(x,phase,label='Outward aberration');c.plot(x,2*phase,label='Mirror round trip');c.plot(x,np.zeros_like(x),label='Conjugate round trip');c.set(xlabel='Transverse coordinate (chosen units)',ylabel='Phase error (rad)',title='Original lossless thin-screen example');c.legend(frameon=False)
m=np.linspace(-12,12,600);d.plot(m,np.sinc(m/(2*np.pi))**2);d.set(xlabel=r'Longitudinal mismatch $\Delta kL$',ylabel='Normalized small-signal conversion',title='Finite length tolerates small mismatch');d.axvline(0,color='gray',ls=':',lw=1)
fig.savefig('paper-1-four-wave-mixing.png',dpi=150);plt.close(fig)
