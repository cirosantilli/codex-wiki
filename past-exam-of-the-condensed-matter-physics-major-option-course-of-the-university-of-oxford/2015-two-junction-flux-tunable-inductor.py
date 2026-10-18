from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axs=plt.subplots(1,2,figsize=(11.6,5.1),layout='constrained')
ax=axs[0]
for yy in [-.8,.8]:
 ax.plot([0,2.15],[yy,yy],color='#174c75',lw=2);ax.plot([2.85,5],[yy,yy],color='#174c75',lw=2);ax.add_patch(Rectangle((2.15,yy-.12),.7,.24,fc='#e8d2b9',ec='black'));ax.text(2.5,yy+.22,r'$I_C$',ha='center')
ax.plot([0,0],[-.8,.8],color='#174c75',lw=2);ax.plot([5,5],[-.8,.8],color='#174c75',lw=2)
ax.annotate('I',xy=(0,0),xytext=(-1,0),va='center',arrowprops=dict(arrowstyle='->',lw=1.5));ax.annotate('I',xy=(6,0),xytext=(5,0),va='center',arrowprops=dict(arrowstyle='->',lw=1.5))
ax.text(2.5,0,r'$\Phi$',ha='center',va='center',fontsize=23);ax.text(3.8,1.1,r'$\delta_1$',ha='center');ax.text(3.8,-1.3,r'$\delta_2$',ha='center');ax.set(xlim=(-1.2,6.2),ylim=(-1.6,1.6),title='Stated ideal two-junction circuit');ax.axis('off')
ax=axs[1];f=np.linspace(0,2,1600);c=np.abs(np.cos(np.pi*f));ax.plot(f,2*c,color='#174c75',lw=2,label=r'$I_{max}/I_C$');bx=ax.twinx();L=np.where(c>.065,1/np.maximum(c,1e-12),np.nan);bx.plot(f,L,color='#b35b15',lw=1.6,label='stable inductance')
for ff in [.5,1.5]:ax.axvline(ff,color='gray',ls=':',lw=1)
ax.set(xlabel=r'$\Phi/\Phi_0$',ylabel=r'$I_{max}/I_C$',ylim=(0,2.3),title='Positive inductance on the stable branch');bx.set(ylabel=r'$L/(\Phi_0/4\pi I_C)$',ylim=(0,10));ax.legend(loc='upper center',frameon=False,fontsize=10);ax.grid(alpha=.15)
fig.suptitle('Flux interference and the small-signal inductive response',fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
