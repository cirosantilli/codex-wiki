"""Original coordinate-region sketches. Python 3.14; NumPy 2.3.5,
Matplotlib 3.10.7. Writes paper-3-change-of-variables.png in the caller's
CWD only; respects the caller's MPLCONFIGDIR.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

def main():
    fig,axes=plt.subplots(1,2,figsize=(8.0,3.9),dpi=130,facecolor='white')
    ax=axes[0];y=np.linspace(0,1/np.sqrt(2),500)
    lo=np.sqrt(1+y*y);hi=np.sqrt(2-y*y)
    ax.fill_betweenx(y,lo,hi,color='#c8dbef')
    ax.plot(lo,y,color='#a84b29',lw=2,label='$x^2-y^2=1$')
    ax.plot(hi,y,color='#245c9b',lw=2,label='$x^2+y^2=2$')
    ax.plot([1,np.sqrt(2)],[0,0],color='0.2',lw=2)
    for x0,y0,label,offset in [(1,0,'$(1,0)$',(-22,-24)),(np.sqrt(2),0,r'$(\sqrt{2},0)$',(0,9)),(np.sqrt(1.5),1/np.sqrt(2),r'$(\sqrt{3/2},1/\sqrt{2})$',(-65,15))]:
        ax.scatter([x0],[y0],color='0.2',s=15);ax.annotate(label,(x0,y0),xytext=offset,textcoords='offset points',fontsize=8)
    ax.set(xlim=(0.85,1.65),ylim=(-0.18,1.05),xlabel='$x$',ylabel='$y$',title='Original region')
    ax.set_aspect('equal');ax.legend(fontsize=8,loc='upper right')
    ax=axes[1]
    ax.add_patch(Polygon([(1,1),(2,1),(2,2)],facecolor='#c8dbef',edgecolor='none'))
    ax.plot([1,2],[1,1],color='#a84b29',lw=2,label='$v=1$')
    ax.plot([2,2],[1,2],color='#245c9b',lw=2,label='$u=2$')
    ax.plot([1,2],[1,2],color='0.2',lw=2,label='$u=v$')
    for p,offset in [((1,1),(-30,-19)),((2,1),(6,-16)),((2,2),(6,4))]:
        ax.scatter([p[0]],[p[1]],color='0.2',s=15);ax.annotate(str(p),p,xytext=offset,textcoords='offset points',fontsize=8)
    ax.set(xlim=(0.75,2.35),ylim=(0.75,2.35),xlabel='$u$',ylabel='$v$',title=r'Transformed region: $1\leq v\leq u\leq2$')
    ax.set_aspect('equal');ax.legend(fontsize=8,loc='upper left')
    fig.tight_layout(w_pad=1.5);fig.savefig('paper-3-change-of-variables.png',facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
