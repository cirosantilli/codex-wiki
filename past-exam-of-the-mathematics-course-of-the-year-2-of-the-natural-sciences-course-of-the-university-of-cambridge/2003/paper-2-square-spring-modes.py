"""Original displacement patterns for four masses joined by all six springs."""
from pathlib import Path
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def main():
    plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.facecolor':'white'})
    positions=np.array([[-1,1],[1,1],[-1,-1],[1,-1]],dtype=float)
    modes=[('Rigid rotation',r'$\omega^2=0$',[1,1,1,-1,-1,1,-1,-1]),('Breathing',r'$\omega^2=4k/m$',[-1,1,1,1,-1,-1,1,-1]),('Vertical mode',r'$\omega^2=2k/m$',[0,1,0,-1,0,-1,0,1]),('Horizontal mode',r'$\omega^2=2k/m$',[1,0,-1,0,-1,0,1,0])]
    fig,axes=plt.subplots(2,2,figsize=(8.6,7.4),dpi=120,layout='constrained')
    for ax,(name,freq,raw) in zip(axes.flat,modes):
        for i,j in itertools.combinations(range(4),2):
            edge=positions[[i,j]]
            ax.plot(edge[:,0],edge[:,1],color='0.73',lw=1.3,zorder=1)
        ax.scatter(positions[:,0],positions[:,1],s=48,color='#227ca6',zorder=4)
        displacement=np.array(raw,dtype=float).reshape(4,2)*.35
        ax.quiver(positions[:,0],positions[:,1],displacement[:,0],displacement[:,1],angles='xy',scale_units='xy',scale=1,color='#bc682a',width=.009,headwidth=4.1,headlength=5.1,zorder=5)
        for i,(x,y) in enumerate(positions):ax.text(.80*x,.80*y,str(i+1),ha='center',va='center',fontsize=10,color='0.25',bbox={'facecolor':'white','edgecolor':'none','pad':.2})
        ax.set(xlim=(-1.65,1.65),ylim=(-1.65,1.65),xticks=[-1,0,1],yticks=[-1,0,1],xlabel='x',ylabel='y',title=name+'\n'+freq)
        ax.set_aspect('equal')
        ax.grid(alpha=.13)
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)

if __name__=='__main__':main()
