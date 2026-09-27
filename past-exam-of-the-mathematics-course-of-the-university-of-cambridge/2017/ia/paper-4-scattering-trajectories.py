#!/usr/bin/env python3
"""Original inverse-square scattering sketches for Q10. Python3.14/mpl3.10.7/np2.3.5.
Run from the wiki root; output is under its mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,axs=plt.subplots(1,2,figsize=(8.8,4.2),layout='constrained')
# Unit incoming speed, impact parameter and absolute coupling: e=sqrt(2).
e=np.sqrt(2); rmax=18
for ax,sgn,title in zip(axs,[-1,1],['Attraction: $k=-1$','Repulsion: $k=+1$']):
    phi_max=np.arccos((1/rmax+sgn)/e)
    phi=np.linspace(phi_max,-phi_max,1600)
    radius=1/(e*np.cos(phi)-sgn)
    beta=np.arctan2(1,-sgn)
    x=radius*np.cos(phi+beta);y=radius*np.sin(phi+beta)
    ax.plot(x,y,color='#174d82',lw=2.3)
    ax.axhline(1,color='gray',ls='--',lw=1,label='incoming asymptote')
    p=np.sqrt(2)+sgn;xp,yp=p*np.cos(beta),p*np.sin(beta)
    ax.plot([0,xp],[0,yp],color='#b02e32',ls=':',lw=1.5)
    ax.scatter([0,xp],[0,yp],color=['black','#b02e32'],s=[25,30],zorder=3)
    ax.annotate('$O$',(0,0),xytext=(5,-12),textcoords='offset points')
    ax.annotate('$p$' if sgn<0 else '$\\widetilde p$',(xp,yp),xytext=(8,4),textcoords='offset points')
    # Arrows follow decreasing polar angle, the incoming-to-outgoing direction.
    for i in (430,1160):
        ax.annotate('',(x[i+40],y[i+40]),(x[i],y[i]),arrowprops={'arrowstyle':'->','color':'#174d82','lw':2})
    ax.annotate('',(-6.7,1),(-6.7,0),arrowprops={'arrowstyle':'<->','color':'black'})
    ax.text(-6.45,.4,'$b=1$',fontsize=10)
    ax.set(xlim=(-8,3),ylim=(-5,7),xlabel='$x$',ylabel='$y$',title=title,aspect='equal')
    ax.grid(alpha=.15)
    ax.text(-7.6,5.6,r'$v=1,\ |k|=1$',fontsize=10)
output=Path('paper-4-scattering-trajectories.png')
output.parent.mkdir(parents=True,exist_ok=True)
fig.savefig(output,dpi=100,facecolor='white');plt.close(fig)
