"""Two-neuron phase portrait; Python 3.14, root-pinned NumPy and Matplotlib.

Output the PNG basename in the caller's CWD. Respect its MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    m, sigma, a, tau = 10., 12., 3., 10.
    g = lambda z: m*a*a*z*z/(sigma*sigma+a*a*z*z)
    points = np.linspace(0, 10.5, 151)
    X,Y = np.meshgrid(points,points)
    fig,ax = plt.subplots(figsize=(6.,4.8),dpi=140,facecolor='white')
    ax.streamplot(points,points,(g(Y)-X)/tau,(g(X)-Y)/tau,
                  color='#b5bdc4',density=1.,linewidth=.65,arrowsize=.9)
    z=np.linspace(0,10.5,400)
    ax.plot(g(z),z,color='#176dab',lw=2.,label=r'$\dot x=0:\ x=g(y)$')
    ax.plot(z,g(z),color='#d68115',lw=2.,label=r'$\dot y=0:\ y=g(x)$')
    ax.plot([0,10.5],[0,10.5],'--',color='#7e8993',lw=.7)
    ax.scatter([0,8],[0,8],s=48,color='#252d35',zorder=5)
    ax.scatter([2],[2],s=58,marker='D',facecolor='white',edgecolor='#252d35',zorder=5)
    ax.annotate('stable (0, 0)',(0,0),xytext=(1.1,.2),fontsize=9)
    ax.annotate('saddle (2, 2)',(2,2),xytext=(3.2,1.2),fontsize=9,
                arrowprops={'arrowstyle':'-','color':'#58636c'})
    ax.annotate('stable (8, 8)',(8,8),xytext=(7.0,9.0),fontsize=9,
                arrowprops={'arrowstyle':'-','color':'#58636c'})
    ax.set(xlim=(-.2,10.6),ylim=(-.2,10.6),xlabel='Activity x',ylabel='Activity y')
    ax.set_aspect('equal')
    ax.legend(loc='upper left',fontsize=9,framealpha=1.)
    ax.set_title('Two-neuron rate dynamics\nm = 10, σ = 12, a = 3, τ = 10',fontsize=11)
    fig.tight_layout()
    fig.savefig(Path.cwd()/'paper-73-neural-phase.png',facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':main()
