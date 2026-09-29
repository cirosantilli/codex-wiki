"""Original triangular-pulse evolution. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run in the mirrored _media directory; the white PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np

x=np.linspace(-3,3,2401)
fig,axes=plt.subplots(1,3,figsize=(10,3.8),facecolor='white',sharey=True)
for ax,t in zip(axes,[0,.4,1.4]):
    right=.5*np.maximum(1-np.abs(x-t),0)
    left=.5*np.maximum(1-np.abs(x+t),0)
    ax.plot(x,left,color='#b75130',lw=1.5,ls='--')
    ax.plot(x,right,color='#26759a',lw=1.5,ls=':')
    ax.plot(x,left+right,color='#25384e',lw=2)
    ax.set(xlim=(-3,3),ylim=(-.025,1.08),xlabel='$x$',title=f'$t={t:g}$')
    ax.grid(alpha=.17);ax.spines[['top','right']].set_visible(False)
    ax.set_xticks([-2,0,2]);ax.set_yticks([0,.5,1])
axes[0].set_ylabel('$u(x,t)$')
fig.suptitle('A triangular displacement released from rest',fontsize=15,y=.98)
handles=[Line2D([],[],color='#25384e',lw=2,label='Total displacement'),Line2D([],[],color='#b75130',ls='--',label='Left-moving half'),Line2D([],[],color='#26759a',ls=':',label='Right-moving half')]
fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,.065),ncol=3,frameon=False,fontsize=10)
fig.text(.5,.015,'Wave speed is 1; initial height and half-width are 1. Corner lines propagate with the pulses.',ha='center',fontsize=10)
fig.subplots_adjust(left=.065,right=.985,top=.8,bottom=.28,wspace=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
plt.close(fig)
