"""Original explanatory figure. Python 3.14, matplotlib 3.10, numpy 2.3. Run from mirrored _media directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc,Polygon
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(9,4));ax=axs[0];th=np.arange(6)*np.pi/3;verts=np.c_[2/3*np.cos(th),2/3*np.sin(th)];ax.add_patch(Polygon(verts,facecolor='#e4f1f5',edgecolor='#254758'))
for i,(x,y) in enumerate(verts):ax.plot(x,y,'ko',ms=3);ax.text(x*1.14,y*1.14,'K' if i%2==0 else "K′",ha='center',va='center',fontsize=9)
for b,label in [(np.array([1,1/np.sqrt(3)]),'b1'),(np.array([-1,1/np.sqrt(3)]),'b2')]:
 ax.annotate('',xy=b,xytext=(0,0),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#b56d21'});ax.text(b[0],b[1]+.09,label,ha='center')
ax.plot(.5,1/(2*np.sqrt(3)),'o',color='#b44e43',ms=4);ax.text(.48,.19,'M');ax.text(0,-.1,'Γ',ha='center');ax.axhline(0,color='.8',lw=.7);ax.axvline(0,color='.8',lw=.7);ax.set(xlim=(-1.2,1.2),ylim=(-.9,.9),aspect='equal',xlabel='kx / (2π/a)',ylabel='ky / (2π/a)')
theta=np.linspace(0,2*np.pi/3,501);local=theta%(np.pi/3);rad=(1/np.sqrt(3))/np.cos(local-np.pi/6);k=2*np.pi*rad[:,None]*np.c_[np.cos(theta),np.sin(theta)];b=1/np.sqrt(3);delta=np.array([[0,b],[.5,-b/2],[-.5,-b/2]]);f=np.exp(1j*k@delta.T).sum(axis=1)
axs[1].plot(theta*180/np.pi,2*np.abs(f),color='#196e9c',lw=2);axs[1].set(xlabel='Radial orientation to zone boundary (degrees)',ylabel='Local band separation / t',xticks=[0,30,60,90,120],xticklabels=['K\n0','M\n30',"K′\n60",'M\n90','K\n120'],ylim=(-.08,2.2));axs[1].grid(alpha=.15);fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
