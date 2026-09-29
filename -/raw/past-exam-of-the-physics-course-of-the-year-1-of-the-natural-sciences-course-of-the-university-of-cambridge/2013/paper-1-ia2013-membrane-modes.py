"""Original rectangular mechanical-membrane mode maps.
Python 3.14, NumPy, Matplotlib; writes PNG basename to cwd.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
x=np.linspace(0,1,301);y=np.linspace(0,.8,241);X,Y=np.meshgrid(x,y)
fig,axes=plt.subplots(1,2,figsize=(8.6,4.1),layout='constrained')
for ax,p,label in [(axes[0],1,r'$f_{11}=\sqrt{41}\,c/(8a)$'),(axes[1],2,r'$f_{21}=\sqrt{89}\,c/(8a)$')]:
 Z=np.sin(p*np.pi*X)*np.sin(np.pi*Y/.8)
 im=ax.pcolormesh(X,Y,Z,cmap='RdBu_r',vmin=-1,vmax=1,shading='auto',rasterized=True)
 ax.add_patch(Rectangle((0,0),1,.8,fill=False,edgecolor='black',lw=2))
 if p==2:ax.axvline(.5,color='black',ls='--',lw=1.3)
 for j in range(p):
  pos=((j+.5)/p,.4);ax.plot(*pos,'o',color='white',ms=19,markeredgecolor='black',mew=.6);ax.text(*pos,'+' if j%2==0 else '−',ha='center',va='center',weight='bold',fontsize=13)
 ax.set(xlim=(0,1),ylim=(0,.8),aspect='equal',xlabel=r'$x/a$',ylabel=r'$y/a$',title=label)
fig.colorbar(im,ax=axes,shrink=.8,label='Instantaneous displacement / peak amplitude')
fig.suptitle('Fixed boundaries are nodes; marked circles are signed antinodes',fontsize=12)
fig.savefig('paper-1-ia2013-membrane-modes.png',dpi=140,facecolor='white')
