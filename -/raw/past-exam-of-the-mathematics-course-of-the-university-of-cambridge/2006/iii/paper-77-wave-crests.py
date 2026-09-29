"""Original wave sketch: Python 3.14, NumPy 2.3.5, matplotlib 3.10.7.
Writes paper-77-wave-crests.png to caller CWD; honors caller MPLCONFIGDIR.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
k,omega,N=1.,.6,1.
m=-k*np.sqrt(N*N/omega**2-1)
fig,ax=plt.subplots(figsize=(7.2,4.5),dpi=150,facecolor='white')
x=np.linspace(-5,8,1200)
for j in range(-3,4):
 z=(2*np.pi*j-k*x)/m;mask=(z>.14)&(z<5.4)
 ax.plot(x[mask],z[mask],color='#286a9b',lw=1.7)
ax.plot(x,.07*np.sin(k*x),color='#333333',lw=2)
ax.annotate('boundary travels right',xy=(2.3,-.35),xytext=(-2.4,-.35),arrowprops={'arrowstyle':'->','color':'#333'},fontsize=10)
ax.annotate('',xy=(5.8,3.8),xytext=(3.4,2.0),arrowprops={'arrowstyle':'->','color':'#b86121','lw':2})
ax.text(3.1,4.2,'energy / group velocity',color='#9b4c17',fontsize=10)
ax.annotate('',xy=(.4,.5),xytext=(-1.4,2.9),arrowprops={'arrowstyle':'->','color':'#81509c','lw':2})
ax.text(-4.5,2.8,'phase propagation',color='#75418f',fontsize=10)
ax.text(4.2,.65,'crests rise to the right',rotation=np.degrees(np.arctan(-k/m)),color='#286a9b',fontsize=10)
ax.set(xlim=(-5,8),ylim=(-.7,5.5),xlabel='Horizontal position x',ylabel='Height z',title='Upward-radiating internal wave from a right-moving boundary')
ax.set_aspect('equal');ax.grid(alpha=.12);fig.tight_layout()
fig.savefig(Path('paper-77-wave-crests.png'),facecolor='white',transparent=False);plt.close(fig)
