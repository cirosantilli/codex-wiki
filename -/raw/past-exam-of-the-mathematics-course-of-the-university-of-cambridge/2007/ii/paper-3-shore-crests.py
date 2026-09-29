"""Original shallow-water crest/ray sketch; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from the desired output directory. Uses a supplied MPLCONFIGDIR unchanged.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Representative p=1, omega/sqrt(g alpha)=1, conserved alongshore K=0.6.
# k_x=-x**(-1/2): crest phase=-2 sqrt(x)+K y; ray y=y0-(2 K/3)x**(3/2).
K=0.6
x=np.linspace(0.00001,0.5,1800)
fig,ax=plt.subplots(figsize=(7.0,4.6),dpi=120,facecolor='white')
for level in np.arange(-2.2,1.31,0.32):
    y=(level+2*np.sqrt(x))/K
    mask=(y>=-1.1)&(y<=1.1)
    ax.plot(x[mask],y[mask],color='#286396',lw=1.5)
for y0 in [-0.72,0.,0.72]:
    y=y0-(2*K/3)*x**1.5
    ax.plot(x,y,color='#b75a22',lw=1.8,ls='--')
    j=np.searchsorted(x,0.32)
    ax.annotate('',xy=(x[j-140],y[j-140]),xytext=(x[j],y[j]),arrowprops={'arrowstyle':'->','color':'#b75a22','lw':1.7})
ax.axvline(0,color='#202020',lw=3)
ax.text(0.008,1.02,'shoreline',fontsize=10,ha='left',va='top')
ax.plot([],[],color='#286396',label='wavecrests (equal phase)')
ax.plot([],[],color='#b75a22',ls='--',label='incident rays')
ax.set(xlim=(-0.006,0.5),ylim=(-1.1,1.1),xlabel='distance offshore, x',ylabel='alongshore coordinate, y')
ax.set_title('Shallow-water approach to a beach: representative p = 1')
ax.legend(loc='lower right',fontsize=9,framealpha=1)
ax.grid(alpha=0.15)
fig.tight_layout()
fig.savefig('paper-3-shore-crests.png',facecolor='white',transparent=False)
plt.close(fig)
