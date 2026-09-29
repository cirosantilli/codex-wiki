from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
n=8;delta=0.12;s=np.r_[np.ones(n//2),-np.ones(n//2)]
p=0.5-delta/2+delta*np.outer(s,s)/2;np.fill_diagonal(p,0)
signal=np.outer(s,s)
fig,axs=plt.subplots(1,2,figsize=(7.2,3.3),dpi=100,facecolor='white')
a=axs[0].imshow(p,cmap='Blues',vmin=0,vmax=.5);axs[0].set_title('Expected adjacency $A_0$');axs[0].set_xticks([1.5,5.5],['group 1','group 2']);axs[0].set_yticks([1.5,5.5],['group 1','group 2']);axs[0].axvline(3.5,color='gray',lw=.8);axs[0].axhline(3.5,color='gray',lw=.8);fig.colorbar(a,ax=axs[0],fraction=.045,pad=.04,ticks=[0,.38,.5])
b=axs[1].imshow(signal,cmap='RdBu',vmin=-1,vmax=1);axs[1].set_title(r'Community signal $M_0\propto ss^T$');axs[1].set_xticks([1.5,5.5],['group 1','group 2']);axs[1].set_yticks([1.5,5.5],['group 1','group 2']);axs[1].axvline(3.5,color='gray',lw=.8);axs[1].axhline(3.5,color='gray',lw=.8);fig.colorbar(b,ax=axs[1],fraction=.045,pad=.04,ticks=[-1,1])
fig.subplots_adjust(left=.10,right=.96,bottom=.16,top=.86,wspace=.65)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=100,facecolor='white',transparent=False)
plt.close(fig)
