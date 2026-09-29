"""Illustrative ON/OFF receptive field; Python 3.14 and root-pinned dependencies.

Output the PNG basename in the caller's CWD. Respect its MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    x=np.linspace(-1.7,1.7,300)
    y=np.linspace(-2.1,2.1,350)
    X,Y=np.meshgrid(x,y)
    kernel=np.exp(-X*X/(2*.53**2)-Y*Y/(2*1.15**2))*np.cos(2*np.pi*X/1.3)
    fig,ax=plt.subplots(figsize=(5.4,4.6),dpi=140,facecolor='white')
    image=ax.imshow(kernel,origin='lower',extent=(x[0],x[-1],y[0],y[-1]),
                    cmap='RdBu_r',vmin=-1,vmax=1,interpolation='bilinear')
    for xx,label in [(0.,'ON'),(-.6,'OFF'),(.6,'OFF')]:
        ax.text(xx,.1,label,ha='center',va='center',fontsize=10,
                bbox={'facecolor':'white','edgecolor':'none','alpha':.85,'pad':2})
    ax.set(xlabel='Horizontal position (arbitrary units)',ylabel='Vertical position (arbitrary units)',
           title='Illustrative simple-cell receptive field')
    bar=fig.colorbar(image,ax=ax,shrink=.83,pad=.04)
    bar.set_label('Signed sensitivity',fontsize=10)
    bar.set_ticks([-1,0,1])
    fig.tight_layout()
    fig.savefig(Path.cwd()/'paper-73-receptive-field.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
