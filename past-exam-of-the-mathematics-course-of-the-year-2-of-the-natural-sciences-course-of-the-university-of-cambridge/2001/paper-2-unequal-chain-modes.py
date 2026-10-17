"""Original unequal three-mass chain modes; Python 3.14, numpy 2.3, matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def main():
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    fig,axes=plt.subplots(3,1,figsize=(7.7,6.2),dpi=120,layout='constrained')
    modes=[('Translation',r'$\omega^2=0$', [1,1,1]),('Lower vibrational mode',r'$\omega^2=k/m$',[-3,0,1]),('Upper vibrational mode',r'$\omega^2=3k/m$',[1,-2,1])]
    pos=np.array([-1.45,0,1.45])
    radii=np.array([.16,.20,.24])
    for ax,(name,freq,vec) in zip(axes,modes):
        for j in range(2):
            start=pos[j]+radii[j]
            end=pos[j+1]-radii[j+1]
            sx=np.linspace(start,end,35)
            sy=np.zeros_like(sx)
            sy[2:-2]=np.where(np.arange(31)%2,.065,-.065)
            ax.plot(sx,sy,color='0.45',lw=1.2+0.45*j,zorder=1)
            ax.text((start+end)/2,-.24,['$k$','$3k$'][j],ha='center',va='top',color='0.3')
        for j,(x,rad,amplitude) in enumerate(zip(pos,radii,vec)):
            ax.add_patch(Circle((x,0),rad,facecolor='#d7e9f3',edgecolor='#1b608a',lw=1.5,zorder=3))
            ax.text(x,0,['$m$','$2m$','$3m$'][j],ha='center',va='center',fontsize=10)
            ax.text(x,-.42,r'$x_'+str(j+1)+'$',ha='center',color='0.4',fontsize=10)
            if amplitude:
                ax.annotate('',xy=(x+.21*amplitude,.36),xytext=(x,.36),arrowprops={'arrowstyle':'-|>','color':'#ae5b28','lw':2})
            else:
                ax.text(x,.36,'stationary',ha='center',va='center',color='#ae5b28',fontsize=9)
        ax.set(xlim=(-2.25,2.25),ylim=(-.55,.60),title=name+'   '+freq)
        ax.set_aspect('equal')
        ax.axis('off')
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
