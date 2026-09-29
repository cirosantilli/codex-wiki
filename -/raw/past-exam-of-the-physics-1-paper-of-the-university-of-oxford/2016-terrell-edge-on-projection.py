from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon, Rectangle
plt.rcParams.update({'font.size':13,'axes.titlesize':14,'figure.facecolor':'white','axes.facecolor':'white'})
beta=.75;ga=1/np.sqrt(1-beta**2);v=np.array([[-.5,-.5],[.5,-.5],[.5,.5],[-.5,.5]])
contracted=np.column_stack([v[:,0]/ga,v[:,1]])
emission=np.column_stack([v[:,0]/ga-beta*v[:,1],v[:,1]])
rotated=np.column_stack([v[:,0]/ga-beta*v[:,1],beta*v[:,0]+v[:,1]/ga])
fig,axs=plt.subplots(2,2,figsize=(12,9.5),layout='constrained');colors=['#0072B2','#D55E00','#009E73','#CC79A7']
for ax,pts,title in zip(axs.flat,[v,contracted,emission,rotated],['Rest-frame square','Simultaneous laboratory positions','Emission events at equal arrival time','Stationary square rotated by arcsin(beta)']):
 ax.add_patch(Polygon(pts,fill=False,lw=2,color='.3'))
 for j,(x,y) in enumerate(pts):
  ax.scatter(x,y,s=55,color=colors[j],zorder=4);ax.text(x+.035,y+.025,'ABCD'[j],color=colors[j],fontsize=12)
 ax.axhline(0,color='.85',lw=.8);ax.axvline(0,color='.85',lw=.8);ax.set(xlim=(-.95,.95),ylim=(-1.05,1.05),aspect='equal',xlabel='transverse coordinate',ylabel='depth coordinate');ax.set_title(title)
for ax,pts in [(axs[1,0],emission),(axs[1,1],rotated)]:
 for j,(x,y) in enumerate(pts):
  ax.plot([x,x],[y,-.85],'--',lw=.9,color=colors[j]);ax.scatter(x,-.85,color=colors[j],s=35)
 ax.plot([-.9,.9],[-.85,-.85],color='.2');ax.text(0,-1.01,'same transverse image coordinates',ha='center',fontsize=11)
axs[0,0].text(0,-.85,'Velocity along +x; camera along -y',ha='center',fontsize=11)
axs[0,1].text(0,-.85,r'$x=X/\gamma$',ha='center')
axs[1,0].text(0,.90,r'$x=X/\gamma-\beta Y$',ha='center')
axs[1,1].text(0,.90,r'$x=X\cos\theta-Y\sin\theta$',ha='center')
fig.suptitle(r'An edge-on relativistic photograph: $\beta=0.75$, apparent rotation $48.6^\circ$; lower-left points are not simultaneous',fontsize=14)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white');plt.close(fig)
