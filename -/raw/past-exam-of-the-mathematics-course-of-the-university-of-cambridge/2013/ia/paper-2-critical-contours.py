"""Opaque contour sketch; Python3.14, NumPy2.3.5, Matplotlib3.10.7.
Writes only its PNG basename to cwd; caller supplies MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():
    fig,ax=plt.subplots(figsize=(9,6.5),dpi=100,facecolor='white')
    grid=np.linspace(-1.3,1.3,1001);X,Y=np.meshgrid(grid,grid)
    Z=X**2-X**4-Y**4+Y**8
    neg=ax.contour(X,Y,Z,levels=[-.6,-.24,-.15,-.05],colors='#2468b4',linewidths=.9)
    pos=ax.contour(X,Y,Z,levels=[.05,.15,.24,.6],colors='#b84931',linewidths=.9)
    ax.clabel(neg,fontsize=8);ax.clabel(pos,fontsize=8)
    yy=np.linspace(-1.15,1.15,500)
    ax.plot(yy**2,yy,'k',lw=1.6);ax.plot(-yy**2,yy,'k',lw=1.6,label='Exact zero curves')
    t=np.linspace(0,2*np.pi,1001)
    ax.plot(np.cos(t),np.sign(np.sin(t))*np.sqrt(np.abs(np.sin(t))),'k',lw=1.6)
    a=2**-.5;b=2**-.25
    ax.scatter([-a,a],[0,0],c='#b84931',s=70,marker='o',label='Strict maxima')
    ax.scatter([0,0],[-b,b],c='#2468b4',s=70,marker='s',label='Strict minima')
    ax.scatter([0,-a,a,-a,a],[0,-b,-b,b,b],c='#bb7900',s=65,marker='x',label='Saddles')
    for x,y,txt in [(-a,0,'M'),(a,0,'M'),(0,-b,'m'),(0,b,'m'),(0,0,'S')]:
        ax.annotate(txt,(x,y),xytext=(8,8),textcoords='offset points',fontsize=11)
    ax.axhline(0,color='0.6',lw=.5);ax.axvline(0,color='0.6',lw=.5)
    ax.set(xlim=(-1.3,1.3),ylim=(-1.3,1.3),xlabel='$x$',ylabel='$y$',title=r'Contours of $x^2-x^4-y^4+y^8$: nine critical points')
    ax.set_aspect('equal');ax.legend(loc='upper left',fontsize=9,facecolor='white',framealpha=1)
    fig.tight_layout();fig.savefig(Path.cwd()/'paper-2-critical-contours.png',dpi=100,facecolor='white',transparent=False);plt.close(fig)
if __name__=='__main__':main()
