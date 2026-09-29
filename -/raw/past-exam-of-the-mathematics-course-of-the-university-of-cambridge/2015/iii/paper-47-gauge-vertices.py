"""Gauge-vertex sketches; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
def wave(ax,a,b):
    a=np.asarray(a);b=np.asarray(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d)
    t=np.linspace(0,1,301);p=a+t[:,None]*d+.025*np.sin(14*np.pi*t)[:,None]*n
    ax.plot(p[:,0],p[:,1],color='#215c91',lw=1.8)
fig,axs=plt.subplots(1,2,figsize=(8,3),dpi=100,facecolor='white')
for ax,ends,labels,title in [
    (axs[0],[(.1,.2),(.9,.2),(.5,.85)],[r'$a,\mu$',r'$b,\nu$',r'$c,\rho$'],r'Cubic: $g\epsilon^{abc}$ and one derivative'),
    (axs[1],[(.1,.2),(.9,.2),(.1,.85),(.9,.85)],[r'$b,\mu$',r'$c,\nu$',r'$d,\rho$',r'$e,\sigma$'],r'Quartic: $g^2\epsilon\epsilon$ and no derivative')]:
    ax.set_facecolor('white')
    for end,label in zip(ends,labels):
        wave(ax,(.5,.5),end);ax.text(end[0],end[1]+(.04 if end[1]>.5 else -.07),label,ha='center',fontsize=12)
    ax.plot(.5,.5,'o',color='#222222',ms=4);ax.set(xlim=(0,1),ylim=(0,1),title=title);ax.axis('off')
fig.subplots_adjust(left=.035,right=.965,bottom=.06,top=.8,wspace=.2)
fig.savefig(Path.cwd()/'paper-47-gauge-vertices.png',facecolor='white',transparent=False)
plt.close(fig)
