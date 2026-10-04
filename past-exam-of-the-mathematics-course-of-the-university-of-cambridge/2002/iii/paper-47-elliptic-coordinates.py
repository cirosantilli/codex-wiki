"""Original elliptic-coordinate sketch; writes its PNG basename to caller CWD.

Python 3.14, NumPy 2.3.5 and Matplotlib 3.10.7. Caller supplies MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 6), dpi=140, facecolor='white')
ax.set_facecolor('white')
xi = np.linspace(0, 2.0, 400)
colors = ['#617b91', '#2a8e77', '#5b69ac', '#b07f2c'] * 2
labels = [r'$\eta=0$',r'$\eta=\pi/4$',r'$\eta=\pi/2$',r'$\eta=3\pi/4$',r'$\eta=\pi$',r'$\eta=5\pi/4$',r'$\eta=3\pi/2$',r'$\eta=7\pi/4$']
for n in range(8):
    eta=n*np.pi/4
    x=np.cosh(xi)*np.cos(eta)
    y=np.sinh(xi)*np.sin(eta)
    ax.plot(x,y,color=colors[n],lw=1.6)
    t=1.32
    tx=np.cosh(t)*np.cos(eta);ty=np.sinh(t)*np.sin(eta)
    offsets={0:(.13,.12),1:(.06,.12),2:(.1,.06),3:(-.48,.12),4:(-.45,.12),5:(-.48,-.22),6:(.1,-.1),7:(.06,-.22)}
    dx,dy=offsets[n]
    ax.text(tx+dx,ty+dy,labels[n],color=colors[n],fontsize=10)
eta=np.linspace(0,2*np.pi,500)
ax.plot(np.cosh(1)*np.cos(eta),np.sinh(1)*np.sin(eta),color='#bd4b43',lw=2.1)
ax.text(1.56,.53,r'$\xi=1$',color='#bd4b43',fontsize=12)
ax.plot([-1,1],[0,0],color='#242424',lw=4,solid_capstyle='round',zorder=5)
ax.text(.2,.15,r'$\xi=0$: crack',fontsize=11,color='#242424')
ax.scatter([-1,1],[0,0],color='#242424',s=22,zorder=6)
ax.text(-1.13,-.23,r'$-a$',fontsize=11);ax.text(.94,-.23,r'$a$',fontsize=11)
ax.set(xlim=(-2.7,2.7),ylim=(-2.05,2.05),xlabel=r'$x/a$',ylabel=r'$y/a$')
ax.set_aspect('equal',adjustable='box')
ax.set_title('Elliptic coordinates around a line crack',pad=15,fontsize=15)
ax.grid(alpha=.15)
fig.tight_layout()
fig.savefig(Path.cwd()/'paper-47-elliptic-coordinates.png',facecolor='white',transparent=False)
plt.close(fig)
