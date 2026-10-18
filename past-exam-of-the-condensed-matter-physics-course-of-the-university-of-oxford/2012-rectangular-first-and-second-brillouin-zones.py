"""Original Brillouin-zone construction; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,Patch

fig,axs=plt.subplots(1,2,figsize=(11.4,6.5),layout='constrained',facecolor='white')
for ax,r in zip(axs,[1.4,3.]):
    K,L=1.,r
    right=np.array([[K,-L],[2*K,-L+K*K/L],[2*K,L-K*K/L],[K,L]])
    top=np.array([[-K,L],[K,L],[0,L+K*K/L]])
    ax.add_patch(Polygon([[-K,-L],[K,-L],[K,L],[-K,L]],facecolor='#bfdbfe',edgecolor='#1d4ed8',lw=2,zorder=3))
    for vertices in [right,right*np.array([-1,1]),top,top*np.array([1,-1])]:
        ax.add_patch(Polygon(vertices,facecolor='#fed7aa',edgecolor='#c2410c',lw=2,zorder=2))
    t=np.linspace(-2.5,2.5,400)
    for sign in [-1,1]:
        ax.plot(t,sign*(K*K+L*L-K*t)/L,color='#78716c',lw=1,ls='--',alpha=.55)
        ax.axvline(sign*2*K,color='#78716c',lw=1,ls=':',alpha=.7)
    ax.axvline(0,color='#64748b',lw=.7);ax.axhline(0,color='#64748b',lw=.7)
    ax.text(0,0,'I',ha='center',va='center',fontsize=18,color='#1d4ed8')
    ax.text(1.46,0,'II',ha='center',va='center',fontsize=14,color='#9a3412')
    ax.annotate('(K, L)',xy=(K,L),xytext=(1.14,L+.33),fontsize=9,arrowprops=dict(arrowstyle='-',color='#475569'))
    ax.text(-.95,L+K*K/L+.15,'(0, L + K²/L)',fontsize=9)
    ax.set(xlim=(-2.45,2.45),ylim=(-L-K*K/L-.5,L+K*K/L+.65),xlabel=r'$k_x/(\pi/a)$',ylabel=r'$k_y/(\pi/a)$',title=f'a/b = {r:g}; K = 1, L = {r:g}')
    ax.set_aspect('equal');ax.grid(alpha=.15)
fig.legend(handles=[Patch(facecolor='#bfdbfe',edgecolor='#1d4ed8',label='First zone'),Patch(facecolor='#fed7aa',edgecolor='#c2410c',label='Second zone')],loc='outside lower center',ncol=2,frameon=False)
fig.suptitle('Crossing exactly one Bragg plane gives the second zone',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
