"""Exact initially-rest electron orbits in non-null crossed fields. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'figure.facecolor':'white'})
# Dimensionless units c=m=|q|=B=1; position unit ell=mc/(|q|B).
fig,axes=plt.subplots(2,2,figsize=(10,7.5),layout='constrained')
E=1.5;V=1/E;G=1/np.sqrt(1-V*V);a=-E/G
T=np.linspace(0,2.8,700);s=a*T
xp=-G*V*T;yp=G/a*(np.cosh(s)-1)
x=G*G*V*(np.sinh(s)/a-T)
axes[0,0].plot(xp,yp,color='#a4472c',lw=2)
axes[0,1].plot(x,yp,color='#a4472c',lw=2)
axes[0,0].set_title(r'Electric-dominated adapted frame: $B^{\prime}=0$')
axes[0,1].set_title(r'Electric-dominated lab: $E/(cB)=1.5$')
V=.5;G=1/np.sqrt(1-V*V);omega=-1/(G*G)
tp=np.linspace(0,4*np.pi/abs(omega),1500);s=omega*tp
xp=-V/omega*np.sin(s);yp=V/omega*(1-np.cos(s))
x=G*V*(tp-np.sin(s)/omega)
axes[1,0].plot(xp,yp,color='#245fa0',lw=2)
axes[1,1].plot(x,yp,color='#245fa0',lw=2)
axes[1,0].set_title(r'Magnetic-dominated adapted frame: $E^{\prime}=0$')
axes[1,1].set_title(r'Magnetic-dominated lab: $E/(cB)=0.5$')
axes[1,0].set_aspect('equal',adjustable='datalim')
for row in range(2):
    for col in range(2):
        ax=axes[row,col]
        ax.scatter([0],[0],color='black',s=25,zorder=4)
        ax.annotate('start',(0,0),xytext=(6,5),textcoords='offset points')
        ax.axhline(0,color='#777777',lw=.6);ax.axvline(0,color='#777777',lw=.6)
        ax.grid(alpha=.2);ax.margins(.12)
        ax.set_xlabel(r'$x^{\prime}/\ell$' if col==0 else r'$x/\ell$')
        ax.set_ylabel(r'$y^{\prime}/\ell$' if col==0 else r'$y/\ell$')
fig.suptitle('Electron trajectories: drift plus electric acceleration or magnetic gyration',fontsize=15)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
