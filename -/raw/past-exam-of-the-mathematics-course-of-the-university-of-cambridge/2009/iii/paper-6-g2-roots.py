"""Python 3.14 / matplotlib 3.10: opaque PNG basename to caller CWD.
Preserve caller MPLCONFIGDIR. G2 short-root-first numbering.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def main():
    a1=np.array([1.,0.]); a2=np.array([-1.5,np.sqrt(3)/2])
    roots=[(1,0),(0,1),(1,1),(2,1),(3,1),(3,2)]
    labels=[r'$\alpha_1$',r'$\alpha_2$',r'$\alpha_1+\alpha_2$',r'$2\alpha_1+\alpha_2=\omega_1$',r'$3\alpha_1+\alpha_2$',r'$3\alpha_1+2\alpha_2=\omega_2$']
    fig,ax=plt.subplots(figsize=(8,7.4),dpi=135,facecolor='white'); short=[]; long=[]
    for k,((u,v),label) in enumerate(zip(roots,labels)):
        p=u*a1+v*a2; isshort=np.dot(p,p)<2; col='#276fbf' if isshort else '#c66a0b'
        (short if isshort else long).extend([p,-p])
        for sign in [1,-1]:
            q=sign*p
            ax.annotate('',xy=q,xytext=(0,0),arrowprops=dict(arrowstyle='->',lw=1.4,color=col),zorder=2)
            ax.scatter(*q,s=28,color=col,zorder=3)
        offset={0:(16,-17),1:(-5,15),2:(-16,12),3:(20,15),4:(14,14),5:(15,16)}[k]
        ax.annotate(label,xy=p,xytext=offset,textcoords='offset points',ha='right' if k in [1,2] else 'left',fontsize=11,color='#17212d')
    for pts,col in [(short,'#276fbf'),(long,'#c66a0b')]:
        pts=sorted(pts,key=lambda p:np.arctan2(p[1],p[0])); pts=np.array(pts+[pts[0]])
        ax.plot(pts[:,0],pts[:,1],ls='--',lw=.8,alpha=.6,color=col)
    for p in [2*a1+a2,3*a1+2*a2]: ax.scatter(*p,s=220,facecolors='none',edgecolors='#923184',lw=2,zorder=4)
    ax.scatter(0,0,s=15,color='#17212d'); ax.text(.07,-.15,'0',fontsize=10)
    ax.axhline(0,color='#c4c4c4',lw=.6,zorder=0); ax.axvline(0,color='#c4c4c4',lw=.6,zorder=0)
    ax.set(aspect='equal',xlim=(-2.45,2.5),ylim=(-2.05,2.25)); ax.axis('off')
    fig.suptitle('G₂ roots and fundamental weights (short root numbered first)',fontsize=13,y=.975)
    fig.text(.5,.035,'Blue: short roots     Orange: long roots     Purple rings: fundamental weights',ha='center',fontsize=10)
    fig.tight_layout(rect=(0,.055,1,.945),pad=.8)
    fig.savefig(Path('paper-6-g2-roots.png'),facecolor='white',transparent=False); plt.close(fig)

if __name__=='__main__': main()
