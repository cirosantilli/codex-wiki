"""Plot exact theta-method absolute stability inequalities; PNG goes to CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def main():
    x=np.linspace(-4,2,901);y=np.linspace(-3,3,901)
    xx,yy=np.meshgrid(x,y)
    fig,axes=plt.subplots(1,3,figsize=(11.5,3.7),layout='constrained')
    labels=['Forward Euler: theta = 0','Trapezoidal: theta = 1/2','Backward Euler: theta = 1']
    for ax,theta,label in zip(axes,[0,.5,1],labels):
        level=2*xx+(1-2*theta)*(xx**2+yy**2)
        ax.pcolormesh(x,y,(level<0).astype(float),cmap=ListedColormap(['white','#d5ebd2']),shading='auto',rasterized=True)
        ax.contour(x,y,level,levels=[0],colors=['#286b36'],linewidths=1.4)
        ax.axhline(0,color='0.6',lw=.6);ax.axvline(0,color='0.6',lw=.6)
        ax.set(xlabel='Re(z)',ylabel='Im(z)',title=label,xlim=(-4,2),ylim=(-3,3),aspect='equal')
    fig.savefig(Path.cwd()/'2011-theta-stability.png',dpi=120,facecolor='white')
    plt.close(fig)


if __name__=='__main__':
    main()
