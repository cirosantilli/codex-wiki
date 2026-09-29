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

segments=[(np.array([0.,0.]),np.array([.5,0.])),(np.array([.5,0.]),np.array([.5,.5])),(np.array([.5,.5]),np.array([0.,0.]))];path=np.concatenate([np.linspace(a,b,200,endpoint=False) for a,b in segments]+[np.array([[0.,0.]])]);s=np.arange(len(path))/200;fig,axs=plt.subplots(1,2,figsize=(9,4.1))
for ax,v in zip(axs,[.03,.22]):
 ex=levels(path[:,0],v);ey=levels(path[:,1],v);e1=ex[:,0]+ey[:,0];e2=np.minimum(ex[:,1]+ey[:,0],ex[:,0]+ey[:,1]);ax.plot(s,e1,lw=2,label='Band 1');ax.plot(s,e2,lw=2,label='Band 2');e1max=2*levels([.5],v)[0,0];e2min=levels([0],v)[0,0]+levels([.5],v)[0,1];ax.axhline(e1max,color='steelblue',ls=':',lw=1);ax.axhline(e2min,color='darkorange',ls=':',lw=1);ax.axhspan(min(e1max,e2min),max(e1max,e2min),color='lightcoral' if e1max>e2min else 'lightgreen',alpha=.25);ax.set(xlim=(0,3),ylim=(-.1,1.1),xticks=[0,1,2,3],xticklabels=['Γ','X','M','Γ'],ylabel='Energy / E_Q',title=f'V₀/E_Q = {v:.2f}: '+('indirect overlap' if e1max>e2min else 'positive global gap'));ax.legend(fontsize=8);ax.grid(alpha=.15)
fig.suptitle('Insulating occupation of the first band also requires two electrons per cell (α = √π)');fig.tight_layout(rect=(0,0,1,.93))

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
