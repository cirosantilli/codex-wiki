"""Original illustration for the 2016 Oxford Mathematical Methods II solution.
Run from any output directory; writes only the matching PNG to that directory.
Tested with Python 3.14, numpy 2.3.5 and matplotlib 3.10.7 (root pyproject.toml).
"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({"font.size": 11, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})

fig,axs=plt.subplots(2,3,figsize=(11,6.5),layout='constrained',gridspec_kw={'height_ratios':[1,1.4]})
t=np.linspace(0,4*np.pi,700);colors=['#2069a8','#b44026','#23925b'];shapes=[np.ones(3),np.array([1,0,-1]),np.array([1,-1,1])];freq=[0,1,np.sqrt(2)]
titles=['Rigid translation: zero frequency',r'Outer antisymmetric: $\omega$',r'Outer symmetric: $\sqrt{2}\omega$']
for j,(v,w,title) in enumerate(zip(shapes,freq,titles)):
 ax=axs[0,j];ax.plot([0,2],[0,0],color='.5',lw=1.2);ax.scatter([0,1,2],[0,0,0],s=[180,300,180],color=colors,edgecolors='white',zorder=3)
 for i in range(3):
  ax.text(i,-.26,['$m$','$2m$','$m$'][i],ha='center')
  if v[i]:ax.annotate('',(i+.3*v[i],.3),(i,.3),arrowprops={'arrowstyle':'->','color':colors[i],'lw':2.5})
  else:ax.text(i,.33,'fixed',ha='center',fontsize=9,color=colors[i])
 ax.set(xlim=(-.5,2.5),ylim=(-.5,.7),title=title);ax.axis('off')
 ax=axs[1,j]
 for i in range(3):
  # Translation is displayed with unit constant velocity; other two start at maximum displacement.
  y=t/(2*np.pi) if j==0 else v[i]*np.cos(w*t)
  ax.plot(t/(2*np.pi),y,color=colors[i],label=f'atom {i+1}',linestyle=['-','--',':'][i],lw=2)
 ax.axhline(0,color='.65',lw=.7);ax.grid(alpha=.2);ax.set(xlabel=r'$t\omega/(2\pi)$',ylabel=r'$x_i/A$',xlim=(0,2))
 ax.set_title('Common uniform drift' if j==0 else 'Displacement histories',fontsize=11)
 if j==0:ax.legend(loc='upper left',fontsize=9)
fig.suptitle(r'Free triatomic chain, $M=2m$, with $\omega=\sqrt{k/m}$'+'\nArrows show one instant of relative motion; translation need not oscillate',fontsize=13)
fig.savefig(Path.cwd()/'2016-triatomic-normal-modes.png',dpi=130,transparent=False)
plt.close(fig)
