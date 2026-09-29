"""Homology HR diagram, Python 3.14 / pinned NumPy and Matplotlib.

Emit the PNG basename in the caller's CWD; respect supplied MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

mass=np.linspace(.6,2.0,150)
zams_T=(3/8)*np.log10(mass)
zams_L=3*np.log10(mass)
X=np.linspace(1,.52,180)
L=2/(1+X)*(8/(3+5*X))**4
R=(X*(1+X)/2)**(1/16)*(8/(3+5*X))**(9/16)
T=(L/R**2)**.25
x,y=np.log10(T),np.log10(L)
fig,ax=plt.subplots(figsize=(6.0,4.2),dpi=150,facecolor='white')
ax.set_facecolor('white')
ax.plot(zams_T,zams_L,lw=2,color='#245f91',label='Zero-age sequence: slope 8')
ax.plot(x,y,lw=2.2,color='#a34024',label='Fixed-mass, fully mixed track')
ax.scatter([0],[0],s=35,color='black',zorder=5)
ax.annotate('Reference star: $X=1$',xy=(0,0),xytext=(-.007,-.45),fontsize=9,arrowprops={'arrowstyle':'->','color':'black'})
k=75
ax.annotate('',xy=(x[k+18],y[k+18]),xytext=(x[k],y[k]),arrowprops={'arrowstyle':'-|>','color':'#a34024','lw':2})
ax.annotate('Hydrogen depletion\ninitial slope $256/53$',xy=(x[95],y[95]),xytext=(.065,.03),fontsize=9,color='#a34024')
ax.set_xlim(.17,-.10)
ax.set_ylim(-.8,1.0)
ax.set_xlabel(r'$\log_{10}(T_e/T_{e,0})$ (hotter to the left)')
ax.set_ylabel(r'$\log_{10}(L/L_0)$')
ax.set_title('Radiative stellar homology and complete mixing',fontsize=11)
ax.grid(alpha=.22)
ax.legend(loc='upper right',fontsize=8,framealpha=1)
fig.tight_layout()
fig.savefig('paper-63-homology-track.png',facecolor='white',transparent=False)
plt.close(fig)
