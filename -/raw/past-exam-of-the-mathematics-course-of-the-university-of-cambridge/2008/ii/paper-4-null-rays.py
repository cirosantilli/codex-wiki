"""Ingoing-chart Schwarzschild null rays; Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Writes paper-4-null-rays.png to caller CWD; preserves MPLCONFIGDIR.
"""
import os
import tempfile
if 'MPLCONFIGDIR' not in os.environ:
    os.environ['MPLCONFIGDIR']=tempfile.mkdtemp(prefix='paper-4-null-rays-mpl-')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(6.2,5.6),layout='constrained',facecolor='white')
ax.set_facecolor('white')
r=np.linspace(.02,2.8,800)
for j,v in enumerate([-2,0,2,4,6]):
    ax.plot(r,v-r,color='#246ca7',lw=1.2,label='Ingoing: v constant' if j==0 else None)
for j,u in enumerate([-4,-2,0,2,4,6]):
    for inside in [True,False]:
        x=np.linspace(.015,.995,800) if inside else np.linspace(1.005,2.8,800)
        y=u+x+2*np.log(np.abs(x-1))
        ax.plot(x,y,color='#b75b32',lw=1.2,label='Outgoing null family' if j==0 and inside else None)
ax.axvline(1,color='#333333',ls='--',lw=1.8,label='Horizon: r = 2M')
ax.axvline(0,color='black',lw=3)
ax.text(.04,5.5,'Singularity',rotation=90,va='top',fontsize=9)
# Future arrows: all ingoing rays move left; outgoing rays move left inside and right outside.
for x,u in [(.6,4),(1.65,0)]:
    dx=-.065 if x<1 else .065
    y=lambda z:u+z+2*np.log(abs(z-1))
    ax.annotate('',xy=(x+dx,y(x+dx)),xytext=(x,y(x)),arrowprops={'arrowstyle':'->','color':'#b75b32','lw':1.8})
ax.annotate('',xy=(1.65,.35),xytext=(1.8,.2),arrowprops={'arrowstyle':'->','color':'#246ca7','lw':1.8})
ax.set_xlim(0,2.8);ax.set_ylim(-6,6)
ax.set_xlabel(r'$r/(2M)$');ax.set_ylabel(r'$\hat t/(2M)$')
ax.set_title('Future light rays in a regular ingoing chart')
ax.legend(loc='lower right',fontsize=8);ax.grid(alpha=.15)
fig.savefig('paper-4-null-rays.png',dpi=150,facecolor='white',transparent=False)
plt.close(fig)
