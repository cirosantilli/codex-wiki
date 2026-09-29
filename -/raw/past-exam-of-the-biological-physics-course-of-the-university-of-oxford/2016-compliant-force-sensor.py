"""Original conceptual figure; Python 3.14, numpy and matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})

from matplotlib.patches import Circle,Rectangle
fig,ax=plt.subplots(figsize=(9,3.7),constrained_layout=True,facecolor='white')
ax.add_patch(Circle((1.5,1.1),.45,fc='#d0ebff',ec='#1864ab',lw=2));ax.add_patch(Circle((1.25,1.1),.62,fill=False,ec='#74c0fc',ls='--',lw=2));ax.plot([1.5,5.6],[1.1,1.1],color='.4',lw=2)
ax.add_patch(Rectangle((5.6,.55),1.6,1.1,fc='#f3f0ff',ec='#7048e8',lw=2));x=np.linspace(5.75,7.05,200);ax.plot(x,1.1+.27*np.sin(9*np.pi*(x-5.75)),color='#7048e8',lw=1.3)
ax.plot([7.2,8],[1.1,1.1],color='.4',lw=2);ax.plot([8,8],[.3,1.9],color='.3',lw=5)
ax.annotate('',xy=(1.5,1.95),xytext=(1.25,1.95),arrowprops={'arrowstyle':'<->','color':'#1864ab'});ax.text(1.38,2.03,r'$\Delta x$',ha='center',color='#1864ab')
ax.text(.3,-.1,'Calibrated optical\nrestoring force',ha='left');ax.text(3.4,.4,'Tension-bearing\ntether',ha='center');ax.text(6.4,-.1,'Generic confined\npolymer load',ha='center');ax.text(8.25,.7,'Fixed\nsupport',ha='left')
ax.text(3.6,2.0,r'$F_{\rm trap}=k_{\rm trap}\Delta x$',ha='center',fontsize=14);ax.set(xlim=(-.05,9),ylim=(-.6,2.5));ax.axis('off');ax.set_title('Conceptual force balance: a compliant sensor measures tension')

fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=130,facecolor='white',transparent=False)
plt.close(fig)
