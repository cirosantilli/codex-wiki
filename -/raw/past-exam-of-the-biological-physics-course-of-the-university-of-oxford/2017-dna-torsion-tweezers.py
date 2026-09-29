"""Original conceptual torsion/extension readout, no protocol; Python 3.14, numpy, matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle,Rectangle,Arc
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(1,2,figsize=(10.7,4.5),gridspec_kw={'width_ratios':[.8,1.3]},constrained_layout=True,facecolor='white')
ax=axs[0];ax.set(xlim=(-1.1,1.1),ylim=(-.15,3.8));ax.axis('off')
ax.add_patch(Rectangle((-.7,0),1.4,.13,facecolor='.72'))
z=np.linspace(.15,2.7,400);xs=.10*np.sin(10*np.pi*z/2.55)
ax.plot(xs,z,lw=1.8,color='#1864ab');ax.plot(-xs,z,lw=1.3,color='#74a9cf')
ax.add_patch(Circle((0,2.93),.29,facecolor='#bdbdbd',edgecolor='.25'))
ax.add_patch(Circle((.12,1.15),.18,facecolor='#fdae6b',edgecolor='#d9480f'))
ax.annotate('Axial force',xy=(0,3.68),xytext=(0,3.34),ha='center',arrowprops={'arrowstyle':'->','lw':1.8})
ax.annotate('Controlled rotation',xy=(.26,3.06),xytext=(-1.02,3.05),fontsize=10,arrowprops={'arrowstyle':'->'})
ax.annotate('Local opening',xy=(.19,1.15),xytext=(.47,.85),fontsize=10,arrowprops={'arrowstyle':'->'})
ax.annotate('',xy=(.72,2.65),xytext=(.72,.13),arrowprops={'arrowstyle':'<->','color':'.3'})
ax.text(.79,1.75,'extension',rotation=90,va='center',fontsize=10)
ax.text(0,-.10,'Torsionally constrained tether',ha='center',fontsize=10)
ax.set_title('Mechanical readout of DNA topology')
n=np.linspace(-5,5,601)
closed=1-.13*np.maximum(abs(n)-1,0);opened=1-.13*np.maximum(abs(n+1)-1,0)
axs[1].plot(n,closed,color='.3',lw=2,label='Before local unwinding')
axs[1].plot(n,opened,color='#1864ab',lw=2,label='After illustrative one-turn unwinding')
for val in [-3,3]:
 a=1-.13*max(abs(val)-1,0);b=1-.13*max(abs(val+1)-1,0)
 axs[1].annotate('',xy=(val,b),xytext=(val,a),arrowprops={'arrowstyle':'->','color':'#d9480f','lw':2})
axs[1].text(-3.8,.63,'Extension rises',color='#d9480f',fontsize=10)
axs[1].text(1.25,.48,'Extension falls',color='#d9480f',fontsize=10)
axs[1].set(xlabel='Imposed linking-number offset (illustrative turns)',ylabel='Relative DNA extension',ylim=(.3,1.07),title='Opposite signals on opposite supercoiling branches')
axs[1].legend(frameon=False,loc='lower center',fontsize=9);axs[1].grid(alpha=.15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
