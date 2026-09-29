"""Generate the original D-meson box diagram; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def line(ax,a,b,reverse=False):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.7)
    a,b=np.array(a),np.array(b);m=(a+b)/2;d=(b-a)*.13
    ax.add_patch(FancyArrowPatch(m+d if reverse else m-d,m-d if reverse else m+d,arrowstyle='-|>',mutation_scale=13,color='black',lw=1))
def wave(ax,a,b):
    a,b=np.array(a),np.array(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d);u=np.linspace(0,1,250)
    xy=a+u[:,None]*d+.013*np.sin(12*np.pi*u)[:,None]*n
    ax.plot(xy[:,0],xy[:,1],color='black',lw=1.5)
fig,ax=plt.subplots(figsize=(7.2,3.8),dpi=100,facecolor='white');ax.set(xlim=(-.05,1.05),ylim=(0,1));ax.axis('off')
ul,ur,ll,lr=(.35,.68),(.65,.68),(.35,.32),(.65,.32)
line(ax,(.11,.84),ul);line(ax,ur,(.89,.84));line(ax,(.11,.16),ll,True);line(ax,lr,(.89,.16),True)
line(ax,ul,ur);line(ax,ll,lr,True);wave(ax,ul,ll);wave(ax,ur,lr)
for p in [ul,ur,ll,lr]:ax.plot(*p,'ko',ms=3.5)
for x,y,label in [(.14,.9,r'$c$'),(.86,.9,r'$u$'),(.14,.08,r'$\bar u$'),(.86,.08,r'$\bar c$'),(.5,.77,r'$d_i$'),(.5,.22,r'$\bar d_j$'),(.26,.5,r'$W^\pm$'),(.75,.5,r'$W^\pm$'),(.01,.5,r'$D^0$'),(.99,.5,r'$\bar D^0$')]:ax.text(x,y,label,ha='center',va='center',fontsize=16)
ax.text(.5,.97,r'$i,j\in\{d,s,b\}$',ha='center',va='center',fontsize=12)
fig.subplots_adjust(left=.04,right=.96,bottom=.02,top=.98)
fig.savefig(Path('paper-305-q3a.png'),facecolor='white',transparent=False);plt.close(fig)
