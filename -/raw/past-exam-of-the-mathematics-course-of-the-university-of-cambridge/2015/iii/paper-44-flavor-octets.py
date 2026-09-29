"""Original flavor-octet diagrams; Python 3.14, Matplotlib 3.10.7."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
fig,axs=plt.subplots(1,2,figsize=(10,5),dpi=100,facecolor='white')
labels=[['$p$','$n$','$\\Sigma^+$','$\\Sigma^-$','$\\Xi^0$','$\\Xi^-$','$\\Sigma^0$','$\\Lambda^0$'],['$K^+$','$K^0$','$\\pi^+$','$\\pi^-$','$\\overline{K}^0$','$K^-$','$\\pi^0$','$\\eta_8$']]
points=[(.5,1),(-.5,1),(1,0),(-1,0),(.5,-1),(-.5,-1),(0,0),(0,0)]
for ax,names,title in zip(axs,labels,['Baryon octet','Pseudoscalar meson octet']):
 ax.set_xlim(-1.6,1.6);ax.set_ylim(-1.5,1.5);ax.set_aspect('equal')
 ax.axhline(0,color='#bbbbbb',lw=.8);ax.axvline(0,color='#bbbbbb',lw=.8)
 ring=[(-.5,1),(.5,1),(1,0),(.5,-1),(-.5,-1),(-1,0),(-.5,1)]
 ax.plot(*zip(*ring),color='#c3cdd7',lw=1)
 ax.scatter(*zip(*points[:6]),color='#163e65',s=55,zorder=3)
 ax.scatter([0],[0],s=85,facecolor='white',edgecolor='#163e65',lw=2,zorder=3)
 for i,((x,y),name) in enumerate(zip(points,names)):
  dx=0 if y else (.17 if x>0 else -.20 if x<0 else .09)
  dy=.18 if y>=0 else -.23
  if i==6:dx=.08;dy=.23
  if i==7:dx=.08;dy=-.29
  ax.text(x+dx,y+dy,name,fontsize=16,ha='center',va='center')
 ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-1,0,1]);ax.set_xlabel('$I_3$',fontsize=13);ax.set_ylabel('$Y=B+S$',fontsize=13)
 ax.set_title(title,fontsize=14);ax.spines[['top','right']].set_visible(False)
fig.subplots_adjust(left=.08,right=.98,top=.88,bottom=.13,wspace=.35)
fig.savefig(Path.cwd()/'paper-44-flavor-octets.png',dpi=100,facecolor='white',transparent=False)
plt.close(fig)
