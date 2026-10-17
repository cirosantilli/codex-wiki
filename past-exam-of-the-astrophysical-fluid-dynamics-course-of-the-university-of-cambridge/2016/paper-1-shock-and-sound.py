"""Original explanatory plot. Tested with Python 3.14, numpy and matplotlib; PNG output goes to the current directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,4.1),layout='constrained')
a=axs[0];gam=5/3;c0=1.;u0=lambda x:.4-.25*x;breaking=3.;t=np.linspace(0,breaking,200);te=np.linspace(breaking,3.7,60)
for x0 in np.linspace(-1,1,9):
 speed=c0+(gam+1)/2*u0(x0);a.plot(x0+speed*t,t,color='#357ba0',lw=1.3);a.plot(x0+speed*te,te,color='#357ba0',lw=.9,ls=':')
a.plot(4.6,3,'o',color='#b85b30');a.annotate('characteristics intersect:\nsmooth solution fails',(4.6,3),(1.2,3.3),ha='center',fontsize=9,arrowprops={'arrowstyle':'->'});a.set(xlim=(-1.2,5.7),ylim=(0,3.8),xlabel='Position (arbitrary units)',ylabel='Time (arbitrary units)',title='Compression steepens into a shock');a.text(1.6,.22,'Faster characteristics catch slower ones.',fontsize=8)
a=axs[1];x=np.linspace(0,2,500);a.plot(x,np.cos(2*np.pi*x),lw=2,color='#357ba0',label='normalized pressure / density perturbation');a.axhline(0,color='#bbb',lw=.8)
q=np.linspace(0,2,45);displ=-.035*np.sin(2*np.pi*q);a.scatter(q+displ,np.full(q.shape,-1.3),s=13,color='#48575f');a.quiver(q[::3]+displ[::3],np.full(q[::3].shape,-1.3),.085*np.cos(2*np.pi*q[::3]),np.zeros(q[::3].shape),angles='xy',scale_units='xy',scale=1,color='#bd6838',width=.005)
a.annotate('wave propagation',(1.8,1.35),(.9,1.35),ha='right',fontsize=9,arrowprops={'arrowstyle':'->'});a.text(1,-1.7,'Dots: displaced fluid elements; arrows: local velocity',ha='center',fontsize=8);a.set(xlim=(-.05,2.05),ylim=(-1.9,1.6),xlabel='Position / wavelength',ylabel='Pressure perturbation (arbitrary units)',title='Longitudinal sound: compression and rarefaction')
fig.savefig('paper-1-shock-and-sound.png',dpi=160);plt.close(fig)
