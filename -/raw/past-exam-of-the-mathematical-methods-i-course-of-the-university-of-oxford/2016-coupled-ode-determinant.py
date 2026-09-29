"""Original illustration for the 2016 Oxford Mathematical Methods I solution.
Writes only the matching PNG to the current working directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

t=np.linspace(0,3,1000);f=np.exp(-3*t)+np.cos(np.sqrt(3)*t)+np.sqrt(3)*np.sin(np.sqrt(3)*t);det=.75+(np.cos(np.sqrt(3)*t)+np.sqrt(3)*np.sin(np.sqrt(3)*t))/8
# Deterministic bisection of the first zero, requiring only numpy.
lo,hi=1.5,1.6
for _ in range(60):
 mid=(lo+hi)/2;val=np.exp(-3*mid)+np.cos(np.sqrt(3)*mid)+np.sqrt(3)*np.sin(np.sqrt(3)*mid)
 if val>0:lo=mid
 else:hi=mid
pole=(lo+hi)/2;star=np.pi/(3*np.sqrt(3));regular=t<pole
fig,axs=plt.subplots(2,1,figsize=(8.7,6.2),layout='constrained',sharex=True)
for ax,y,label in [(axs[0],f,'$f(t)$'),(axs[1],det,r'$\det M$')]:
 ax.plot(t[regular],y[regular],color='#246ca4',lw=2,label='regular coupled solution')
 ax.plot(t[~regular],y[~regular],color='#246ca4',lw=1.8,ls='--',label='formal continuation')
 ax.axvline(pole,color='#a33a2a',ls=':',lw=1.2);ax.axvline(star,color='#398049',ls=':',lw=1.2);ax.grid(alpha=.2);ax.set(ylabel=label,xlim=(0,3))
axs[0].axhline(0,color='.55',lw=.8);axs[0].annotate(r'$g$ has a pole; $f$ remains smooth',(pole,0),(1.65,1.5),arrowprops={'arrowstyle':'->','color':'#a33a2a'},fontsize=10)
axs[0].set_title(r'$f=e^{-3t}+2\cos(\sqrt{3}t-\pi/3)$');axs[0].legend(loc='lower left',fontsize=9)
axs[1].axhline(1,color='black',lw=.9);axs[1].scatter([star],[1],color='#398049',zorder=4);axs[1].annotate(r'first $\det M=1$: $t_*=\pi/(3\sqrt{3})$',(star,1),(.9,.91),arrowprops={'arrowstyle':'->','color':'#398049'},fontsize=10);axs[1].set(xlabel='$t$',ylim=(.46,1.04))
fig.savefig(Path.cwd()/'2016-coupled-ode-determinant.png',dpi=140,transparent=False)
plt.close(fig)
