"""Original normalized second-state densities, including a finite-well solution.

Dimensionless barrier U=100 in units hbar^2/(2mL^2); no source plot is copied.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
U=100.;lo=np.pi+1e-9;hi=2*np.pi-1e-9
for _ in range(90):
 k=(lo+hi)/2;f=k/np.tan(k/2)+np.sqrt(U-k*k)
 if f>0:lo=k
 else:hi=k
k=(lo+hi)/2;kap=np.sqrt(U-k*k);normal=.5-np.sin(k)/(2*k)+np.sin(k/2)**2/kap
x=np.linspace(-.35,1.35,2001)
psi=np.where(x<0,-np.sin(k/2)*np.exp(kap*x),np.where(x>1,np.sin(k/2)*np.exp(-kap*(x-1)),np.sin(k*(x-.5))))/np.sqrt(normal)
p_inf=np.where((x>=0)&(x<=1),2*np.sin(2*np.pi*x)**2,0)
fig,ax=plt.subplots(figsize=(7.8,4.4),layout='constrained',facecolor='white')
ax.plot(x,p_inf,'--',color='.35',lw=2,label='Infinite well: second state')
ax.plot(x,psi**2,color='#245c9f',lw=2,label=f'Finite well: barrier U = {U:.0f}')
for z in [0,1]:ax.axvline(z,color='.6',ls=':')
ax.fill_between(x,0,psi**2,where=(x<0)|(x>1),color='#c7dfef')
ax.annotate('Evanescent tail',(-.08,float(np.interp(-.08,x,psi**2))),(-.28,.65),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.annotate('Central node',(.5,0),(.45,.55),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlim=(-.35,1.35),ylim=(0,2.6),xlabel='Position x/L',ylabel=r'Dimensionless density $L|\psi|^2$',title='Finite walls permit penetration outside the well')
ax.legend(fontsize=10,loc='upper right');ax.spines[['top','right']].set_visible(False)
fig.savefig(Path('paper-1-probability-wells.png'),dpi=130,facecolor='white');plt.close(fig)
