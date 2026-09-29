"""Original educational diagram. Python 3.14, NumPy and Matplotlib; output is saved in the current working directory."""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})
from matplotlib.patches import Circle
th=np.deg2rad(28); u=np.array([np.cos(th),np.sin(th)]); n=np.array([-np.sin(th),np.cos(th)])
c=np.array([0.,0.]); radius=.65; contact=c-radius*n
fig,ax=plt.subplots(figsize=(6.6,4.6),layout='constrained')
ax.add_patch(Circle(c,radius,facecolor='#e7f0f7',edgecolor='#273746',lw=2))
line=np.array([contact-1.7*u,contact+1.6*u]);ax.plot(line[:,0],line[:,1],color='#9aa3aa',lw=3)
ax.scatter(*contact,s=26,color='black',zorder=5);ax.scatter(*c,s=16,color='black')
def arrow(start,end,label,offset=(0,0),color='#225c91'):
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'-|>','lw':2.2,'color':color,'mutation_scale':16})
 p=end+np.array(offset);ax.text(*p,label,ha='center',va='center',color=color,fontsize=12)
arrow(c,c+1.65*u,r'$T$',(.12,.05))
arrow(c,c+np.array([0,-1.5]),r'$Mg$',(.22,0),'#a03a35')
arrow(contact,contact+1.95*n,r'$N$',(-.14,.07),'#34806c')
arrow(contact,contact-1.2*u,r'$F$',(-.12,-.12),'#a47316')
start=c+.95*n;arrow(start,start+.8*u,r'$q>0$',(.16,.03),'#66717a')
ax.text(0,1.65,'Uphill acceleration: static friction points downhill',ha='center',fontsize=11)
ax.text(0,-1.9,r'$Fa=I(q/a),\quad I=Ma^2/2$',ha='center',fontsize=12)
ax.set(xlim=(-1.9,1.9),ylim=(-2.05,1.9),aspect='equal');ax.axis('off')
fig.savefig('paper-1-ia2014-disc-forces.png',dpi=150,facecolor='white');plt.close(fig)
