"""Original solution figure. Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7. Output to CWD."""
OUT='digital-systems-linear-algebra-introduction-to-formal-proof-projection-stretch.png'
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10})
fig,axes=plt.subplots(1,2,figsize=(7.8,3.7),dpi=100,facecolor='white')
for ax in axes:
 ax.set_aspect('equal');ax.axhline(0,color='#bbbbbb',lw=.7);ax.axvline(0,color='#bbbbbb',lw=.7);ax.set_xlim(-1,3.8);ax.set_ylim(-.8,4.1);ax.grid(alpha=.15)
def vec(ax,v,label,color,shift=(0,0)):
 ax.annotate('',v,(0,0),arrowprops={'arrowstyle':'->','lw':2,'color':color});ax.text(v[0]+shift[0],v[1]+shift[1],label,color=color)
a=axes[0];th=np.pi/6;q=np.array([np.cos(th),np.sin(th)]);x=np.array([1.,3.]);p=np.dot(q,x)*q
u=np.linspace(-.9,4,100);a.plot(u*q[0],u*q[1],color='#aaaaaa',lw=1)
vec(a,x,r'$x$','#2166ac',(.05,.05));vec(a,p,r'$(q_1^Tx)q_1$','#a85a12',(.08,-.12));vec(a,q,r'$q_1$','#22744a',(.05,-.15));a.plot([p[0],x[0]],[p[1],x[1]],'--',color='#555555');a.add_patch(Arc((0,0),1.1,1.1,theta1=30,theta2=np.degrees(np.arctan2(x[1],x[0])),color='#555555'));a.text(.44,.48,r'$\phi$');a.set_title('Signed projection on a unit direction',fontsize=10)
a=axes[1];th=np.pi/3;u=np.array([np.cos(th),np.sin(th)]);v=np.array([-u[1],u[0]]);x=1.4*u+.6*v;y=2.8*u+.6*v
r=np.linspace(-1,4.2,100);a.plot(r*u[0],r*u[1],color='#aaaaaa');vec(a,x,r'$x$','#2166ac',(-.55,.03));vec(a,y,r'$Tx$','#a85a12',(.06,.05));
a.plot([x[0],(1.4*u)[0]],[x[1],(1.4*u)[1]],'--',color='#777777');a.plot([y[0],(2.8*u)[0]],[y[1],(2.8*u)[1]],'--',color='#777777');a.text(2.0,3.7,r'$y=\sqrt{3}x$',fontsize=9);a.set_title('Double parallel; preserve perpendicular',fontsize=10)
fig.tight_layout(pad=1.2)
fig.savefig(Path.cwd()/OUT,dpi=100,facecolor='white',transparent=False,metadata={'Software':'codex-wiki Matplotlib'});plt.close(fig)
