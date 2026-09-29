"""Original Bloch x-z sections; save a matching opaque PNG in the CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch
import numpy as np
fig, axes=plt.subplots(1,2,figsize=(11,5.8),dpi=120)
fig.patch.set_facecolor('white')
colors=['#166b9a','#a45517'];root2=np.sqrt(2)
for ax in axes:
    ax.set_facecolor('white');ax.set_aspect('equal');ax.set(xlim=(-1.4,1.4),ylim=(-1.35,1.35));ax.axis('off')
    ax.add_patch(Circle((0,0),1,fill=False,ec='#9aa3a9',lw=1.3))
    ax.axhline(0,color='#c4c9ce',lw=.8);ax.axvline(0,color='#c4c9ce',lw=.8)
    ax.text(1.23,-.07,'x',fontsize=13);ax.text(.04,1.18,'z',fontsize=13)
def state(ax,x,z,label,delta):
    ax.add_patch(FancyArrowPatch((0,0),(x,z),arrowstyle='-|>',mutation_scale=17,lw=2,color=colors[0]))
    ax.text(x+delta[0],z+delta[1],label,fontsize=14,color=colors[0],ha='center')
def measure(ax,n,pluspos,minuspos):
    n=np.asarray(n);ax.plot([-1.08*n[0],1.08*n[0]],[-1.08*n[1],1.08*n[1]],'--',color=colors[1],lw=2)
    ax.text(*pluspos,'+1',fontsize=12,color=colors[1]);ax.text(*minuspos,'−1',fontsize=12,color=colors[1])
state(axes[0],1/root2,1/root2,r'$a$',(.13,.02));state(axes[0],1/root2,-1/root2,r'$b$',(.13,-.04));measure(axes[0],[0,1],(-.22,1.08),(-.22,-1.17))
axes[0].plot([1/root2,1/root2],[-1/root2,1/root2],':',color='#8c969e',lw=1.3)
axes[0].set_title(r'States $a,b$: optimal axis $Z$',fontsize=14,pad=17)
state(axes[1],0,1,r'$|0\rangle$',(.19,.01));state(axes[1],1,0,r'$|+\rangle$',(.08,.16));measure(axes[1],[-1/root2,1/root2],(-1.04,.84),(.82,-.94))
axes[1].set_title(r'States $0,+$: optimal axis $(Z-X)/\sqrt{2}$',fontsize=14,pad=17)
fig.suptitle('Equal-prior discrimination: measure along the difference of Bloch vectors',fontsize=16,y=.98)
fig.text(.5,.045,'Blue arrows: candidate states. Dashed brown line: measurement axis.   State-vector angles are half the Bloch angles.',ha='center',fontsize=11,color='#38434c')
fig.subplots_adjust(top=.81,bottom=.13,wspace=.15,left=.025,right=.975)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),facecolor='white',metadata={'Software':'codex-wiki original figure'})
plt.close(fig)
