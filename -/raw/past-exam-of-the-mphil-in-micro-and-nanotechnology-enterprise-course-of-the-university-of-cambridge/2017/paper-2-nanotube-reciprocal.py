"""Original explanatory figure; Python 3.14, matplotlib 3.10, numpy 2.3. Writes a basename PNG to cwd, normally mirrored _media."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Polygon,Arc
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','axes.facecolor':'white'})

fig,axs=plt.subplots(1,2,figsize=(8,3.6));th=np.arange(6)*np.pi/3+np.pi/6;ax=axs[0];xy=np.c_[np.cos(th),np.sin(th)];ax.add_patch(Polygon(xy,fill=False,lw=2));ax.scatter(xy[:,0],xy[:,1],color='#3c7388');ax.annotate('',xy=(1.2,0),xytext=(-1.2,0),arrowprops={'arrowstyle':'<->'});ax.text(0,-.2,'Circumference direction Ch',ha='center',fontsize=8);ax.annotate('',xy=(0,1.5),xytext=(0,1.05),arrowprops={'arrowstyle':'->'});ax.text(.05,1.35,'Tube axis',fontsize=8);ax.set(xlim=(-1.7,1.7),ylim=(-1.6,1.7),aspect='equal',title='Real carbon-ring hexagon');ax.axis('off')
ax=axs[1];th=np.arange(6)*np.pi/3;xy=np.c_[np.cos(th),np.sin(th)];ax.add_patch(Polygon(xy,facecolor='#e6f0f3',edgecolor='#426777'))
for x in [-.8,-.4,0,.4,.8]:ax.plot([x,x],[-1.2,1.2],color='#b67b31',lw=1)
for i,(x,y) in enumerate(xy):ax.text(x*1.16,y*1.16,'K' if i%2==0 else "K′",ha='center',va='center',fontsize=8)
ax.text(0,-1.5,'Allowed k lines satisfy k · Ch = 2πℓ',ha='center',fontsize=8);ax.set(xlim=(-1.7,1.7),ylim=(-1.6,1.7),aspect='equal',title='Parent graphene reciprocal zone');ax.axis('off');fig.tight_layout()

fig.savefig(Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',bbox_inches='tight');plt.close(fig)
