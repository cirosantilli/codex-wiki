"""Original bound-state intersection sketch; Python 3.14, numpy/matplotlib.
Run in the desired image output directory; writes its local basename PNG.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(.005,np.pi-.005,1300)
fig,ax=plt.subplots(figsize=(6.8,4.5),facecolor='white')
ax.set_facecolor('white')
ax.plot(x,-x/np.tan(x),color='#222222',lw=2,label=r'$\eta=-\xi\cot\xi$')
for radius,color,style in [(1.25,'#777777','--'),(2.4,'#1570a6','-')]:
 z=np.linspace(0,radius,600)
 ax.plot(z,np.sqrt(radius**2-z**2),style,color=color,lw=2,label=fr'$\xi^2+\eta^2=R^2$, $R={radius}$')
ax.axhline(0,color='black',lw=.8)
ax.axvline(np.pi/2,color='#888888',lw=.8,ls=':')
ax.set(xlim=(0,np.pi),ylim=(-1.2,4.0),xlabel=r'$\xi$',ylabel=r'$\eta$',title=r'Odd states require a positive intersection beyond $\pi/2$')
ax.set_xticks([0,np.pi/2,np.pi],[r'$0$',r'$\pi/2$',r'$\pi$'])
ax.grid(alpha=.2)
ax.legend(fontsize=9,loc='upper left')
fig.tight_layout()
fig.savefig(Path(__file__).stem+'.png',dpi=160,facecolor='white')
