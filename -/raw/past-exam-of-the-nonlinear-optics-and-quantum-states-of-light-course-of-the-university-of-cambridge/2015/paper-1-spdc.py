"""Original explanatory figure; Python 3.14, numpy and matplotlib.
Writes a literal PNG basename to cwd. No source-image pixels or media paths.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
plt.rcParams.update({'font.size':10,'figure.facecolor':'white','savefig.facecolor':'white','axes.spines.top':False,'axes.spines.right':False})
fig,(a,b)=plt.subplots(1,2,figsize=(10.5,4),layout='constrained')
for xy,w,h,txt,col in [((-.1,-.2),1.35,.6,'pump','#e9edf1'),((1.8,-.35),1.3,.9,'χ⁽²⁾ crystal','#e7d8ef'),((4,1),1.5,.65,'idler detector','#e0eaf8'),((4,-1.3),1.5,.65,'signal output','#e0eaf8')]:
 a.add_patch(Rectangle(xy,w,h,facecolor=col,edgecolor='gray'));a.text(xy[0]+w/2,xy[1]+h/2,txt,ha='center',va='center',fontsize=9)
for start,end in [((1.25,.1),(1.8,.1)),((3.1,.1),(4,1.3)),((3.1,.1),(4,-1))]:a.annotate('',end,start,arrowprops=dict(arrowstyle='->',lw=2))
a.text(3.9,.25,'herald timestamp',ha='center',fontsize=9);a.text(2.8,-1.8,'Conditional signal ≠ a photon every pump pulse',ha='center',fontsize=10);a.set(xlim=(-.3,5.8),ylim=(-2,2),title='Pair generation and heralding (schematic)');a.axis('off')
u=np.linspace(-3,3,300);x,y=np.meshgrid(u,u);joint=np.exp(-(x+y)**2/.20)*np.sinc((.75*x-.5*y)/np.pi)**2;im=b.imshow(joint,origin='lower',extent=(-3,3,-3,3),aspect='equal',cmap='viridis');b.set(xlabel='Signal detuning (chosen units)',ylabel='Idler detuning (chosen units)',title='Illustrative joint spectral intensity');fig.colorbar(im,ax=b,label='Normalized intensity',shrink=.85)
fig.savefig('paper-1-spdc.png',dpi=150);plt.close(fig)
