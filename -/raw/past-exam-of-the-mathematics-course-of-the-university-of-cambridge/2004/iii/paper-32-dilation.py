"""Python 3.14; numpy 2.3.5 / matplotlib 3.10.7. Emit opaque PNG to caller CWD.
The caller controls MPLCONFIGDIR; this generator leaves it unchanged.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, ax=plt.subplots(figsize=(10,3.3),dpi=130,facecolor='white')
ax.set_facecolor('white');ax.set_xlim(0,10);ax.set_ylim(.1,3.0);ax.axis('off')
def arrow(x1,y1,x2,y2):
 ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops={'arrowstyle':'->','lw':1.7,'color':'#263746'})
def box(x,y,w,h,text):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04',facecolor='#eaf2fa',edgecolor='#315b83',lw=1.7))
 ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=15)
ax.text(.8,2.13,r'System $\rho$',ha='center',va='center',fontsize=15)
ax.text(.8,1.07,r'Environment $|0\rangle\langle0|$',ha='center',va='center',fontsize=14)
arrow(1.9,2.13,3.2,2.13);arrow(1.9,1.07,3.2,1.07)
box(3.25,.72,1.35,1.76,r'$U$')
arrow(4.65,2.13,6.15,2.13);arrow(4.65,1.07,6.15,1.07)
box(6.2,.72,1.6,1.76,'Discard $E$\n'+r'$\mathrm{Tr}_E$')
arrow(7.85,1.6,8.7,1.6)
ax.text(9.15,1.6,r'$\mathcal{E}(\rho)$',ha='center',va='center',fontsize=18)
ax.text(5,2.85,'A quantum channel from unitary coupling and discarding the environment',ha='center',fontsize=14)
fig.tight_layout(pad=.8)
fig.savefig(Path(__file__).with_suffix('.png').name,facecolor='white',transparent=False)
plt.close(fig)
