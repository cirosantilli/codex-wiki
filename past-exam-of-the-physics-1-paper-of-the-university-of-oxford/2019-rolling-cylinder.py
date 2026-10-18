"""Original rolling-cylinder coordinates and fixed-incline force diagram."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Polygon,Arc
import numpy as np

plt.rcParams.update({'font.size':11,'axes.titlesize':12,'figure.facecolor':'white','savefig.facecolor':'white'})
fig,axes=plt.subplots(1,2,figsize=(10.2,4.0),layout='constrained');alpha=np.arctan2(1.6,3.8);t=np.array([np.cos(alpha),np.sin(alpha)]);n=np.array([-np.sin(alpha),np.cos(alpha)])
ax=axes[0];base=np.array([.5,0]);R=.4;s=2.1;p=base+s*t;center=p+R*n;ax.add_patch(Polygon([base,base+[3.8,0],base+[3.8,1.6]],facecolor='#e7e9ec',edgecolor='#555555',linewidth=1.4));ax.axhline(0,color='#555555',linewidth=.9);ax.add_patch(Circle(center,R,facecolor='#dcecf5',edgecolor='#176a9e',linewidth=2));ax.plot(*np.array([center,p]).T,color='#176a9e',linestyle='--');ax.text(center[0]-.13,center[1]+.05,'$M_c$');ax.text(3.65,.35,'$M_b$');ax.text(center[0]+.15,center[1]-.18,'$R$');ax.add_patch(Arc(base,.9,.9,theta1=0,theta2=np.degrees(alpha)));ax.text(1.05,.08,r'$\alpha$')
start=base-.12*n;end=p-.12*n;ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'<->','color':'#b24d25'});mid=(start+end)/2;ax.text(mid[0]-.04,mid[1]-.18,'$s$',color='#b24d25');ax.annotate('',xy=(.5,-.22),xytext=(0,-.22),arrowprops={'arrowstyle':'<->'});ax.text(.25,-.42,'$X$',ha='center');ax.text(2.35,-.6,r'$s$ positive uphill; $\theta$ positive anticlockwise',ha='center',fontsize=9);ax.set(title='Moving wedge: independent coordinates $X,s$',xlim=(-.1,4.6),ylim=(-.7,2));ax.set_aspect('equal');ax.axis('off')
ax=axes[1];R=.55;center=np.array([0.,0]);p=center-R*n;ends=np.array([p-1.5*t,p+1.5*t]);ax.plot(*ends.T,color='#555555',linewidth=1.5);ax.add_patch(Circle(center,R,facecolor='#dcecf5',edgecolor='#176a9e',linewidth=2));ax.plot(*np.array([center,p]).T,color='#888888',linestyle='--')
def arrow(start,vec,label,color,shift=(0,0)):
 end=start+vec;ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','color':color,'linewidth':1.8});ax.text(*(end+np.array(shift)),label,color=color,ha='center')
arrow(p,1.35*n,'$N$','#347b40',(-.12,.02));arrow(p,.95*t,'$f$','#b24d25',(.08,.02));arrow(center,np.array([0,-1.05]),'$M_cg$','#333333',(.25,-.03));ax.text(.08,.15,'$M_c$',fontsize=10);ax.text(-.2,-1.35,r'$N=M_cg\cos\alpha,\quad f=\frac{1}{3}M_cg\sin\alpha$',ha='center',fontsize=10);ax.set(title='Fixed wedge: contact forces',xlim=(-1.45,1.6),ylim=(-1.5,1.2));ax.set_aspect('equal');ax.axis('off')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False,metadata={'Software':'Matplotlib'});plt.close(fig)
