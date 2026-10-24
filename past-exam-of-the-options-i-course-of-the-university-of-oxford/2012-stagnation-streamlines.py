"""Python 3.14; numpy and matplotlib. Write the PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x=np.linspace(-3,3,180);y=np.linspace(0,3,100);X,Y=np.meshgrid(x,y)
fig,ax=plt.subplots(figsize=(7,4),layout='constrained',facecolor='white')
ax.streamplot(x,y,X,-Y,color='#245f83',density=1.05,linewidth=.9,arrowsize=1.1)
# Selected level curves emphasize the exact hyperbolic geometry.
for c in [-3,-1,1,3]:
 xx=np.linspace(.04,3,500)*np.sign(c);yy=c/xx;mask=(yy>=0)&(yy<=3)
 ax.plot(xx[mask],yy[mask],color='#ae5f34',lw=1.5)
ax.axhline(0,color='#303030',lw=3);ax.scatter([0],[0],color='#8f3535',s=30,zorder=5)
ax.text(1.6,.12,'Impermeable wall',fontsize=10,color='#333333')
ax.set(xlabel='$x$',ylabel='$y$',title=r'Stagnation flow: streamlines $xy=c$',xlim=(-3,3),ylim=(-.08,3),aspect='equal')
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'2012-stagnation-streamlines.png',dpi=150,facecolor='white')
