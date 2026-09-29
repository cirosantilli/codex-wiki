"""Quartic planar dynamics. Python 3.14; root NumPy/Matplotlib.
Opaque PNG basename to caller CWD; respect caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


def vector_field(x, y, alpha):
    return .5*alpha*x+y-2*y**3, -x


def main():
    fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), sharey=True)
    x = np.linspace(-1.65, 1.65, 241); y = np.linspace(-1.55, 1.55, 241)
    X, Y = np.meshgrid(x, y); K = X*X+Y*Y-Y**4
    saddle = 1/np.sqrt(2)
    for ax, alpha in zip(axes, [0., .25]):
        U, V = vector_field(X, Y, alpha)
        ax.streamplot(x, y, U, V, color='#35678e', linewidth=.65, arrowsize=1., density=.75)
        ax.contour(X, Y, K, levels=[.04, .12, .21, .45, .8], colors='#b3b3b3', linewidths=.65)
        for sign in [-1, 1]:
            xx = sign*(y*y-.5)
            ax.plot(xx, y, color='#aa4623' if alpha==0 else '#b5a194', lw=1.8 if alpha==0 else 1,
                    ls='-' if alpha==0 else '--', label=r'$K=1/4$' if sign==1 else None)
        ax.scatter([0,0,0],[0,saddle,-saddle],color='#202020',s=22,zorder=5)
        for label, yy in [('O',0),('S+',saddle),('S-',-saddle)]:ax.text(.055,yy+.045,label,fontsize=9)
        ax.set(xlim=(-1.65,1.65),ylim=(-1.55,1.55),xlabel='x')
        ax.set_aspect('equal'); ax.grid(alpha=.1)
        ax.set_title(r'$\alpha=0$: conserved levels' if alpha==0 else r'$\alpha=0.25$: outward $K$ crossing',fontsize=11)
        ax.legend(loc='lower right',fontsize=8)
    axes[0].set_ylabel('y')
    fig.suptitle('Quartic oscillator: centre, saddle connections and escaping trajectories',fontsize=12)
    fig.text(.5,.02,'Solid brown curves are separatrices at zero antidamping; dashed brown curves are reference K-levels in the perturbed panel.',ha='center',fontsize=8)
    fig.tight_layout(rect=(0,.045,1,.93))
    fig.savefig(Path.cwd()/'paper-2-quartic-phase-portrait.png',dpi=120,facecolor='white',transparent=False)
    plt.close(fig)


if __name__ == '__main__': main()
