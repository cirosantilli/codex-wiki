"""Generate original tree-level charm-decay diagrams; Python 3.14, matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def line(ax,a,b,reverse=False):
    ax.plot([a[0],b[0]],[a[1],b[1]],color='black',lw=1.7)
    a,b=np.array(a),np.array(b);m=(a+b)/2;d=(b-a)*.13
    ax.add_patch(FancyArrowPatch(m+d if reverse else m-d,m-d if reverse else m+d,arrowstyle='-|>',mutation_scale=12,color='black',lw=1))
def wave(ax,a,b):
    a,b=np.array(a),np.array(b);d=b-a;n=np.array([-d[1],d[0]])/np.linalg.norm(d);u=np.linspace(0,1,250)
    xy=a+u[:,None]*d+.014*np.sin(12*np.pi*u)[:,None]*n
    ax.plot(xy[:,0],xy[:,1],color='black',lw=1.5)
def bracket(ax,x,y0,y1,label):
    ax.plot([x-.025,x,x,x-.025],[y0,y0,y1,y1],color='black',lw=1.2)
    ax.text(x+.055,(y0+y1)/2,label,ha='left',va='center',fontsize=16)
fig,axes=plt.subplots(1,2,figsize=(10.4,4.5),dpi=100,facecolor='white')
for ax,suppressed in zip(axes,[False,True]):
    ax.set(xlim=(0,1.3),ylim=(-.12,1.08));ax.axis('off')
    v,w=(.40,.58),(.58,.30)
    line(ax,(.08,.83),(.89,.83));line(ax,(.08,.58),v,True);line(ax,v,(.89,.68),True);wave(ax,v,w);line(ax,w,(.89,.34));line(ax,w,(.89,.16),True)
    ax.plot(*v,'ko',ms=3.5);ax.plot(*w,'ko',ms=3.5)
    labels=[(.10,.89,r'$u$'),(.10,.51,r'$\bar c$'),(.84,.9,r'$u$'),(.87,.73,r'$\bar d$' if suppressed else r'$\bar s$'),(.87,.4,r'$s$' if suppressed else r'$d$'),(.85,.09,r'$\bar u$'),(.40,.33,r'$W^-$')]
    for x,y,label in labels:ax.text(x,y,label,ha='center',va='center',fontsize=15)
    bracket(ax,.98,.67,.84,r'$\pi^+$' if suppressed else r'$K^+$');bracket(ax,.98,.15,.35,r'$K^-$' if suppressed else r'$\pi^-$')
    ax.text(.08,.73,r'$\bar D^0$',ha='center',va='center',fontsize=15)
    ax.text(.66,.99,'Doubly Cabibbo-suppressed' if suppressed else 'Cabibbo-favoured',ha='center',fontsize=12)
    ax.text(.65,-.065,r'$V_{cd}V_{us}^{*}$' if suppressed else r'$V_{cs}V_{ud}^{*}$',ha='center',fontsize=15)
fig.subplots_adjust(left=.02,right=.98,bottom=.025,top=.98,wspace=.08)
fig.savefig(Path('paper-305-q3c.png'),facecolor='white',transparent=False);plt.close(fig)
