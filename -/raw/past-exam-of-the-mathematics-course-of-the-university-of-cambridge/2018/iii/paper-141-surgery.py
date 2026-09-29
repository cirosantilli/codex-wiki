"""Generate paper-141-surgery.png in CWD; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots(figsize=(8,3),dpi=100)
centres=[-.75,.75]
t=np.linspace(0,2*np.pi,1200)
curves=[np.column_stack((c+np.cos(t),.8*np.sin(t))) for c in centres]
for xy in curves: ax.plot(xy[:,0],xy[:,1],'k',lw=2.3)
# At each pair of crossings, alternate which circle is over: each adjacent pair is a Hopf link.
for left in range(1):
 cross_x=(centres[left]+centres[left+1])/2
 for upper in (True,False):
  cross_y=(1 if upper else -1)*.8*np.sqrt(1-.75**2)
  over=left if upper else left+1
  xy=curves[over]; dist=np.hypot(xy[:,0]-cross_x,xy[:,1]-cross_y)
  i=int(np.argmin(dist));idx=np.arange(i-25,i+26)%len(t)
  ax.plot(xy[idx,0],xy[idx,1],color='white',lw=8,zorder=3)
  ax.plot(xy[idx,0],xy[idx,1],color='black',lw=2.3,zorder=4)
for c,label in zip(centres,[2,3]):ax.text(c,1.12,str(label),ha='center',fontsize=18)
ax.text(0,-1.2,r'$2-1/3=5/3$',ha='center',fontsize=14)
ax.set_xlim(-2.8,2.8);ax.set_ylim(-1.45,1.55);ax.set_aspect('equal');ax.axis('off')
fig.subplots_adjust(left=.03,right=.97,top=.98,bottom=.02)
fig.savefig('paper-141-surgery.png',facecolor='white')
