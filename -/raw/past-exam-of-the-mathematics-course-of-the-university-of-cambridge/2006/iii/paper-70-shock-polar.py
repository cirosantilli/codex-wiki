"""Original strong-shock polar; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Outputs paper-70-shock-polar.png to caller CWD; respects caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

gamma=5/3
centre=gamma/(gamma+1);radius=1/(gamma+1)
t=np.linspace(0,2*np.pi,500)
xt=centre-radius**2/centre;yt=radius*np.sqrt(1-(radius/centre)**2)
fig,ax=plt.subplots(figsize=(6.8,4.3),facecolor='white')
ax.plot(centre+radius*np.cos(t),radius*np.sin(t),color='#1864ab',lw=2.3,label='Strong-shock polar')
ax.plot([0,1.07],[0,0],color='#9ba6ad',lw=.8)
ax.plot([0,0],[-.45,.45],color='#9ba6ad',lw=.8)
ax.plot([0,xt*1.65],[0,yt*1.65],color='#d95f02',lw=1.7,label='Maximum-deflection ray')
ax.plot([centre,xt],[0,yt],color='#2b8a3e',lw=1.5,ls='--',label='Radius at tangency')
ax.scatter([0,centre,xt,1,(gamma-1)/(gamma+1)],[0,0,yt,0,0],color=['#495057','#2b8a3e','#d95f02','#1864ab','#1864ab'],s=28,zorder=5)
angle=np.arcsin(1/gamma);tt=np.linspace(0,angle,40)
ax.plot(.15*np.cos(tt),.15*np.sin(tt),color='#d95f02',lw=1)
ax.text(.13,.065,r'$\delta_{\max}$',color='#d95f02',fontsize=11)
ax.text(centre+.02,-.055,r'$C$',color='#2b8a3e',fontsize=11)
ax.text(xt-.05,yt+.03,r'$T$',color='#d95f02',fontsize=11)
ax.text(1,-.065,'Upstream',ha='center',fontsize=10)
ax.text(.25,-.065,'Normal shock',ha='center',fontsize=9)
ax.set(xlim=(-.06,1.17),ylim=(-.47,.56),xlabel=r'$u_{X2}/|u_1|$',ylabel=r'$u_{Y2}/|u_1|$')
ax.set_aspect('equal');ax.grid(alpha=.17)
ax.set_title(r'$\gamma=5/3$: circle centre $5/8$, radius $3/8$')
fig.tight_layout()
fig.savefig('paper-70-shock-polar.png',dpi=120,facecolor='white',transparent=False)
plt.close(fig)
