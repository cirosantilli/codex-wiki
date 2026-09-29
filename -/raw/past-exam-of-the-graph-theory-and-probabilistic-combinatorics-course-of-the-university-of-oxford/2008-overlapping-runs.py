"""Python 3.14.4; NumPy 2.3.5; Matplotlib 3.10.7. PNG is written in CWD."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
fig,ax=plt.subplots(figsize=(6.7,6.3),layout='constrained',facecolor='white');ax.set_facecolor('white');ax.set_aspect('equal');ax.axis('off')
n=16;ang=np.pi/2-2*np.pi*np.arange(n)/n;x=np.cos(ang);y=np.sin(ang)
ax.plot(np.r_[x,x[0]],np.r_[y,y[0]],c='.7',lw=1)
for i in range(n):
 color='#b28cbb' if i in {2,3,4} else '#377eb8' if i in {0,1} else '#e08214' if i in {5,6} else '.85'
 ax.scatter(x[i],y[i],s=190,c=color,edgecolors='white',zorder=3);ax.text(1.18*x[i],1.18*y[i],str(i+1),ha='center',va='center',fontsize=10)
ax.add_patch(Arc((0,0),2.75,2.75,theta1=0,theta2=90,color='#377eb8',lw=3));ax.add_patch(Arc((0,0),3.05,3.05,theta1=-45,theta2=45,color='#e08214',lw=3))
ax.text(0,-1.65,r'Two length-5 windows, shifted by 2: overlap 3, union 7',ha='center',fontsize=11)
ax.text(0,0,r'Joint success probability: $p^7$'+'\n\n'+r'Independent value would be $p^{10}$',ha='center',va='center',fontsize=12)
ax.set(xlim=(-1.65,1.85),ylim=(-1.85,1.65),title='Why overlapping run indicators have positive covariance')
fig.savefig(Path.cwd()/'2008-overlapping-runs.png',dpi=170,facecolor='white')
