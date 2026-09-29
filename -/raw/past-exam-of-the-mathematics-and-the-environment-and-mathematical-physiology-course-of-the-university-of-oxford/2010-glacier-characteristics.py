"""Original solution diagram. Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7. Output to current working directory."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
plt.rcParams.update({"figure.facecolor":"white","axes.facecolor":"white","font.size":10,"axes.spines.top":False,"axes.spines.right":False})

n=3;q=1/(n+2);p=1-q
fig,axs=plt.subplots(1,3,figsize=(13,3.6),layout='constrained')
x=np.linspace(0,1,500);axs[0].plot(x,1-2*x);axs[0].axhline(0,color='.6',ls=':');axs[0].set(xlabel='x',ylabel='Net accumulation',title='Gain upstream; ablation downstream')
axs[1].plot(x,((n+2)*x*(1-x))**q);axs[1].set(xlabel='x',ylabel='Steady thickness',title='Steady profile (n=3)')
# Regularize both endpoint singularities with y=(1-cos(theta))/2.
theta=np.linspace(1e-8,np.pi-1e-8,2500);y=(1-np.cos(theta))/2
# Use endpoint-safe sin(theta/2)^2 rather than subtraction.
y=np.sin(theta/2)**2
base=(n+2)**(-p)*2**(2*p-1)*np.sin(theta)**(1-2*p)
# Endpoint integral numerically via midpoint grid; finite integrable power.
M=20000;th=(np.arange(M)+.5)*np.pi/M;yy=np.sin(th/2)**2;integrand=(n+2)**(-p)*2**(2*p-1)*np.sin(th)**(1-2*p);tt=np.cumsum(integrand)*np.pi/M
for xi in (0,.1,.2,.3,.4):
 L=1-2*xi;xx=xi+L*yy;times=L**(-n/(n+2))*tt;axs[2].plot(xx,times,label=fr'$\xi={xi:g}$')
axs[2].set(xlabel='x',ylabel='Characteristic travel time',title='Formal family; crossings require care',ylim=(0,6));axs[2].legend(fontsize=7,ncol=2);axs[2].axvline(.5,color='.7',ls=':')
fig.savefig(Path.cwd()/'2010-glacier-characteristics.png',dpi=150,facecolor='white');plt.close(fig)
