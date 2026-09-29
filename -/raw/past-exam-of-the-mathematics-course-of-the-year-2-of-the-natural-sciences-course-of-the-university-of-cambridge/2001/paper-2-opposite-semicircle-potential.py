"""Original harmonic disk potential; Python 3.14, numpy 2.3, matplotlib 3.10."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size':11, 'figure.facecolor':'white', 'axes.facecolor':'white'})
    x = np.linspace(-1.002, 1.002, 501)
    X, Y = np.meshgrid(x, x)
    R2 = X*X+Y*Y
    potential = np.ma.masked_where(R2>=1, 2/np.pi*np.arctan2(2*Y, 1-R2))
    fig, ax = plt.subplots(figsize=(6.8, 6.0), dpi=120, layout='constrained')
    filled = ax.contourf(X, Y, potential, levels=np.linspace(-1,1,41), cmap='RdBu_r', vmin=-1, vmax=1)
    lines = ax.contour(X, Y, potential, levels=np.arange(-.8,.81,.2), colors='0.25', linewidths=.65)
    ax.clabel(lines, fmt='%.1f', fontsize=8, inline=True)
    t = np.linspace(0,np.pi,400)
    ax.plot(np.cos(t),np.sin(t),color='#ac2834',lw=3)
    ax.plot(np.cos(t),-np.sin(t),color='#23689b',lw=3)
    ax.scatter([-1,1],[0,0],facecolor='white',edgecolor='0.25',s=42,zorder=6)
    ax.text(0,1.08,r'$+V_0$',ha='center',color='#ac2834',fontsize=13)
    ax.text(0,-1.12,r'$-V_0$',ha='center',color='#23689b',fontsize=13)
    ax.set(xlim=(-1.18,1.18),ylim=(-1.2,1.2),xlabel='x',ylabel='y',xticks=[-1,0,1],yticks=[-1,0,1],title='Opposite semicircle boundary potentials')
    ax.set_aspect('equal')
    cbar=fig.colorbar(filled,ax=ax,shrink=.78,ticks=[-1,-.5,0,.5,1])
    cbar.set_label(r'$\Phi/V_0$')
    fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
    plt.close(fig)


if __name__=='__main__':
    main()
