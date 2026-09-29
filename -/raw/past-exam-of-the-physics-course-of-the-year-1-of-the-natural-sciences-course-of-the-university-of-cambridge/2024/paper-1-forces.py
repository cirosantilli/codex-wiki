"""Original free-body diagrams; force directions, not scale magnitudes."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
fig,axs=plt.subplots(1,3,figsize=(10,4.2),layout='constrained',facecolor='white')
def force(ax,v,label,colour='#245c9f'):
 ax.annotate('',v,(0,0),arrowprops={'arrowstyle':'->','color':colour,'lw':2})
 ax.text(v[0]*1.13,v[1]*1.13,label,ha='center',va='center',fontsize=12,color=colour)
for ax in axs:
 ax.scatter([0],[0],s=120,color='.25',zorder=4);ax.set(xlim=(-1.5,1.6),ylim=(-1.5,1.6),aspect='equal');ax.axis('off')
force(axs[0],(0,1),'N');force(axs[0],(0,-1),'mg');force(axs[0],(-1,0),'μN')
axs[0].annotate('velocity',(1.2,.5),(.25,.5),arrowprops={'arrowstyle':'->','color':'.4'},color='.4')
a=np.deg2rad(25);t=np.array([np.cos(a),np.sin(a)]);n=np.array([-np.sin(a),np.cos(a)])
axs[1].plot([-1.4*t[0],1.4*t[0]],[-1.4*t[1]-.12,1.4*t[1]-.12],':',color='.6')
force(axs[1],1.15*t,'T');force(axs[1],-.9*t,'μN');force(axs[1],n,'N');force(axs[1],(0,-1.05),'mg')
force(axs[2],(0,1),'T');force(axs[2],(0,-1.1),r'$m_wg$')
for ax,title in zip(axs,['Horizontal parcel','Parcel ascending incline','Descending hanging mass']):ax.set_title(title,fontsize=12)
fig.suptitle('Forces on each body; gravity components are not extra forces',fontsize=13)
fig.savefig(Path('paper-1-forces.png'),dpi=130,facecolor='white');plt.close(fig)
