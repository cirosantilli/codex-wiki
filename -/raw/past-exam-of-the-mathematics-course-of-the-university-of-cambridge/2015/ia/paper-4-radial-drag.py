"""Original bounded radial-drag orbit and energy diagram.
Python 3.14; numpy 2.3.5; matplotlib 3.10.7. Output basename PNG in cwd only.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
phi=np.linspace(0,30,4501);omega=np.sqrt(.91)
u=1+.35*np.exp(-.3*phi)*np.cos(omega*phi)
up=.35*np.exp(-.3*phi)*(-.3*np.cos(omega*phi)-omega*np.sin(omega*phi))
r=1/u;energy=.5*(u*u+up*up)-u
fig,(ax,bx)=plt.subplots(1,2,figsize=(9,10/3),dpi=120,facecolor='white')
circle=np.linspace(0,2*np.pi,361)
ax.plot(np.cos(circle),np.sin(circle),ls='--',color='#555',lw=1,label='limiting circle')
ax.plot(r*np.cos(phi),r*np.sin(phi),color='#1765a1',lw=1.4,label='radially damped orbit')
ax.plot(0,0,'o',color='#ae452c',ms=4);ax.plot(r[0],0,'o',color='#1765a1',ms=4)
ax.annotate('start',xy=(r[0],0),xytext=(1.08,-.45),arrowprops={'arrowstyle':'->','color':'#333'},fontsize=9)
ax.set_aspect('equal');ax.set(xlim=(-1.45,1.45),ylim=(-1.25,1.4),xlabel='x',ylabel='y',title='Radial oscillations approach r = 1')
ax.legend(loc='upper left',fontsize=8,framealpha=1)
bx.plot(phi,energy,color='#1765a1',lw=2);bx.axhline(-.5,color='#555',ls='--',lw=1)
bx.text(12,-.497,'circular energy −1/2',fontsize=9,ha='center',va='bottom')
bx.set(xlim=(0,30),ylim=(-.506,-.426),xlabel='forward angle φ',ylabel='total energy E',title='Energy decreases; angular momentum is fixed')
for panel in (ax,bx):panel.spines[['top','right']].set_visible(False)
fig.tight_layout();fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
