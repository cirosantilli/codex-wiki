"""Original level-curve sketch. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.

Save the white PNG to cwd, normally the corresponding _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2.4,2.4,600);X,Y=np.meshgrid(x,x)
fig,ax=plt.subplots(figsize=(6.0,5.2),layout='constrained',facecolor='white')
levels=[-2,-1,0,1,2]
cs=ax.contour(X,Y,X*Y,levels=levels,colors=['#0072b2','#0072b2','#555555','#d55e00','#d55e00'],linewidths=[1.4,1.6,1.1,1.6,1.4])
labels={-2:r'$e^{-2}$',-1:r'$e^{-1}$',0:r'$1$',1:r'$e$',2:r'$e^2$'}
label_positions=[(1.2,2/1.2),(1.5,1/1.5),(-1.2,2/1.2),(-1.5,1/1.5),
                 (1.2,-2/1.2),(1.5,-1/1.5),(-1.2,-2/1.2),(-1.5,-1/1.5),
                 (0,1.4),(-1.4,0)]
ax.clabel(cs,fmt=labels,inline=True,fontsize=11,manual=label_positions)
ax.scatter([0],[0],color='#333333',s=25,zorder=5)
ax.annotate('Saddle: $f=1$',(0,0),xytext=(.25,.55),arrowprops={'arrowstyle':'->','color':'#555555'},fontsize=11)
ax.set(xlabel='$x$',ylabel='$y$',title=r'Level values of $f(x,y)=e^{xy}$',xlim=(-2.4,2.4),ylim=(-2.4,2.4))
ax.set_aspect('equal');ax.grid(alpha=.14)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=160,facecolor='white')
