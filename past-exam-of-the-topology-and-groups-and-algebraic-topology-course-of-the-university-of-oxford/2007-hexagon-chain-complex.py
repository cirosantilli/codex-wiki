"""Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. PNG output in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon,FancyArrowPatch
th=np.pi/2+2*np.pi*np.arange(6)/6;v=np.c_[np.cos(th),np.sin(th)];tris=[(0,1,2),(2,3,4),(4,5,0),(0,2,4)];colors=['#d9eaf4','#e1efd9','#f8e5ca','#e9dff1']
fig,ax=plt.subplots(figsize=(6.4,6.2),layout='constrained',facecolor='white');ax.set_facecolor('white');ax.set_aspect('equal');ax.axis('off')
for j,t in enumerate(tris):
 ax.add_patch(Polygon(v[list(t)],facecolor=colors[j],edgecolor='none'));c=v[list(t)].mean(axis=0);ax.text(c[0],c[1],rf'$\sigma_{j+1}$',ha='center',va='center',fontsize=14)
for i in range(6):
 j=(i+1)%6;ax.plot(v[[i,j],0],v[[i,j],1],c='black',lw=1.8);p=.35*v[i]+.65*v[j];q=.60*v[i]+.40*v[j];ax.add_patch(FancyArrowPatch(q,p,arrowstyle='-|>',mutation_scale=13,color='black'));m=(v[i]+v[j])/2*1.15;ax.text(*m,['$a$','$a$','$b$','$b$','$c$','$c$'][i],ha='center',va='center',fontsize=13)
for i,j,label in [(0,2,'d'),(2,4,'e'),(4,0,'f')]:
 ax.plot(v[[i,j],0],v[[i,j],1],c='#5e3c99',lw=1.5);p=.4*v[i]+.6*v[j];q=.6*v[i]+.4*v[j];ax.add_patch(FancyArrowPatch(q,p,arrowstyle='-|>',mutation_scale=12,color='#5e3c99'));m=(v[i]+v[j])/2;ax.text(m[0]+.06,m[1]+.04,'$'+label+'$',ha='center',va='center',fontsize=13,color='#5e3c99',bbox={'facecolor':'white','edgecolor':'none','pad':1})
for i,p in enumerate(v):ax.scatter(*p,c='black',s=20);ax.text(*(p*1.22),rf'$v_{i+1}$',ha='center',va='center',fontsize=12)
ax.set(xlim=(-1.35,1.35),ylim=(-1.35,1.38),title='Four faces, six edge classes, one quotient vertex')
fig.savefig(Path.cwd()/'2007-hexagon-chain-complex.png',dpi=170,facecolor='white')
