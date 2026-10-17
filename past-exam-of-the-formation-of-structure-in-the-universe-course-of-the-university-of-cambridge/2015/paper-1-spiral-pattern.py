"""Original analytic solution diagram; Python3.14.4, numpy2.3.5, matplotlib3.10.7.
Run from mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(10.5,4.7));pattern=.65;time=1.5;radii=[.75,1.4];theta=np.linspace(.5,4.5,350)
for ax,t in zip(axs,[0,time]):
 for j in [0,1]:
  r=np.exp(.29*(theta-2.3));phi=theta+j*np.pi+pattern*t;ax.plot(r*np.cos(phi),r*np.sin(phi),color='#909090',lw=6,alpha=.35);ax.plot(r*np.cos(phi),r*np.sin(phi),color='#303030',lw=1)
 for index,r in enumerate(radii):
  phase=np.log(r)/.29+2.3;orbit=1/r;tstar=phase+orbit*t;ax.add_patch(Circle((0,0),r,fill=False,ls=':',ec='#4775a5',alpha=.7));ax.scatter([r*np.cos(tstar)],[r*np.sin(tstar)],s=65,color=['#2166ac','#b2182b'][index],label='Orbit Ω = %.2f'%orbit)
 ax.scatter([0],[0],s=20,c='black');ax.set(aspect='equal',xlim=(-2.2,2.2),ylim=(-2.2,2.2),xlabel='Illustrative position',ylabel='Illustrative position',title='Time %.1f: pattern Ωp = %.2f'%(t,pattern));ax.legend(fontsize=8,loc='lower right')
fig.suptitle('A rotating density crest is distinct from individual stellar orbits');fig.text(.5,.01,'Original kinematic illustration; no claimed fitted galactic parameters or eigenmode.',ha='center',fontsize=9);fig.tight_layout(rect=(0,.05,1,.94))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
