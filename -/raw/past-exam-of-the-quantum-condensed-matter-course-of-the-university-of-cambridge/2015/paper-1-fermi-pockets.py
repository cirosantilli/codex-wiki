"""Original solution diagram; Python 3.14.4, numpy 2.3.5, matplotlib 3.10.7.
Run from the mirrored _media directory; output is a basename in cwd.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})

def levels(q,v,cut=5):
 q=np.atleast_1d(q);g=np.arange(-cut,cut+1);H=np.zeros((len(q),len(g),len(g)));inds=np.arange(len(g));H[:,inds,inds]=(q[:,None]+g[None,:])**2
 for j in range(len(g)-1):H[:,j,j+1]=H[:,j+1,j]=-v/2
 return np.linalg.eigvalsh(H)[:,:3]

alpha=np.sqrt(3);fig,axs=plt.subplots(1,2,figsize=(9.3,4.6));t=np.linspace(0,2*np.pi,800);R=1/alpha;ax=axs[0];ax.plot(R*np.cos(t),R*np.sin(t),color='black',lw=2,label='Free Fermi circle');ax.plot([-.5,.5,.5,-.5,-.5],[-.5,-.5,.5,.5,-.5],color='.4',ls='--');ax.annotate('Q',(.5,-.64),(-.5,-.64),arrowprops={'arrowstyle':'<->'},ha='center');ax.text(0,-.69,'Square side Q',ha='center',fontsize=9);ax.set(title='V₀ = 0, α = √3',xlim=(-.74,.74),ylim=(-.74,.74));ax.legend(fontsize=8,loc='upper right')
q=np.linspace(-.5,.5,401);v=.02;en=levels(q,v);one=en[:,0];two=en[:,1];E1=one[:,None]+one[None,:];Ex=two[:,None]+one[None,:];Ey=one[:,None]+two[None,:];E2=np.minimum(Ex,Ey)
# The periodic mesh excludes one endpoint for the filling determination.
allE=np.sort(np.concatenate([E1[:-1,:-1].ravel(),Ex[:-1,:-1].ravel(),Ey[:-1,:-1].ravel()]));rank=int((np.pi/alpha**2)*400**2);ef=(allE[rank-1]+allE[rank])/2
X,Y=np.meshgrid(q,q,indexing='ij');ax=axs[1];ax.contourf(X,Y,np.where(E1>ef,1,0),levels=[.5,1.5],colors=['mistyrose']);ax.contourf(X,Y,np.where(E2<ef,1,0),levels=[.5,1.5],colors=['lightblue']);ax.contour(X,Y,E1,levels=[ef],colors=['darkred'],linewidths=2);ax.contour(X,Y,E2,levels=[ef],colors=['navy'],linewidths=2);ax.plot([-.5,.5,.5,-.5,-.5],[-.5,-.5,.5,.5,-.5],color='.3');ax.text(.37,.4,'h',color='darkred',fontweight='bold');ax.text(-.45,.02,'e',color='navy',fontweight='bold');ax.text(.02,.43,'e',color='navy',fontweight='bold');ax.scatter([0,.5,.5],[0,0,.5],s=12,color='black');ax.text(.02,-.06,'Γ');ax.text(.43,-.06,'X');ax.text(.42,.43,'M');ax.set(title='V₀ = 0.02 E_Q: weak reconstructed pockets',xlim=(-.56,.56),ylim=(-.56,.56));ax.plot([],[],color='navy',label='Electron pockets (e)');ax.plot([],[],color='darkred',label='Hole pocket (h)');ax.legend(fontsize=8,loc='lower center')
for ax in axs:ax.set(xlabel='kₓ/Q',ylabel='kᵧ/Q');ax.set_aspect('equal');ax.grid(alpha=.12)
fig.suptitle('Opposite zone faces are identified: two electron pockets and one corner hole pocket');fig.tight_layout(rect=(0,.02,1,.94));fig.text(.5,.005,'Finite-potential panel is an original plane-wave calculation at fixed density; V₀/E_Q is illustrative.',ha='center',fontsize=8)

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
