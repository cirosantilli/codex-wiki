"""Original Yukawa fermion triangle. Python 3.14, Matplotlib 3.10.7.
Writes an opaque PNG basename to the caller's CWD; respects MPLCONFIGDIR.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({'font.size': 12, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, ax = plt.subplots(figsize=(6.4, 4.3), dpi=120)
a,b,c=(-.8,0),(.55,.75),(.55,-.75)
for u,v,lab,off in [(a,b,r'$\ell+k_1$',(-.13,.2)),(b,c,r'$\ell$',(.2,0)),(c,a,r'$\ell-k_2$',(-.14,-.2))]:
    ax.plot([u[0],v[0]],[u[1],v[1]],color='#253a55',linewidth=1.8)
    x=(u[0]*.58+v[0]*.42,u[1]*.58+v[1]*.42)
    y=(u[0]*.42+v[0]*.58,u[1]*.42+v[1]*.58)
    ax.add_patch(FancyArrowPatch(x,y,arrowstyle='-|>',mutation_scale=14,linewidth=1.5,color='#253a55'))
    ax.text((u[0]+v[0])/2+off[0],(u[1]+v[1])/2+off[1],lab,ha='center',va='center',bbox={'facecolor':'white','edgecolor':'none','pad':1})
for u,v,lab,off in [((-1.9,0),a,r'$\Phi(P)$',(0,.17)),(b,(1.65,1.15),r'$\phi(k_1)$',(.05,.15)),(c,(1.65,-1.15),r'$\phi(k_2)$',(.05,-.15))]:
    ax.plot([u[0],v[0]],[u[1],v[1]],linestyle='--',color='#a1531b',linewidth=1.8)
    ax.text((u[0]+v[0])/2+off[0],(u[1]+v[1])/2+off[1],lab,ha='center',va='center')
for pos,lab,off in [(a,r'$-iG$',(-.18,-.28)),(b,r'$-ig$',(0,.3)),(c,r'$-ig$',(0,-.3))]:
    ax.scatter(*pos,s=30,color='#253a55',zorder=5);ax.text(pos[0]+off[0],pos[1]+off[1],lab,ha='center')
ax.set_title('Scalar decay through a Dirac fermion loop',pad=14)
ax.set_xlim(-2.05,1.95);ax.set_ylim(-1.6,1.65);ax.set_aspect('equal');ax.axis('off')
fig.text(.5,.04,r'$P=k_1+k_2$; add the reversed fermion orientation as well.',ha='center',fontsize=10)
fig.subplots_adjust(bottom=.13,top=.87)
fig.savefig(Path.cwd()/'paper-48-fermion-triangle.png',facecolor='white',transparent=False)
plt.close(fig)
