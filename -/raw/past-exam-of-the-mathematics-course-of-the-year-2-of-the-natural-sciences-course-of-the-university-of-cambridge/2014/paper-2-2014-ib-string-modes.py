"""Original three-bead transverse-mode sketches. Python 3.14, NumPy 2.3, Matplotlib 3.10.
Run in the corresponding _media directory; the opaque white PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig,axes=plt.subplots(1,3,figsize=(10,4.3),facecolor='white')
x=np.arange(5)
shapes=[(1,np.sqrt(2),1),(1,0,-1),(1,-np.sqrt(2),1)]
frequencies=[r'$\omega_1^2=(2-\sqrt{2})\tau/(m\ell)$',r'$\omega_2^2=2\tau/(m\ell)$',r'$\omega_3^2=(2+\sqrt{2})\tau/(m\ell)$']
labels=[r'$(1,\sqrt{2},1)$',r'$(1,0,-1)$',r'$(1,-\sqrt{2},1)$']
for j,(ax,shape,freq,label) in enumerate(zip(axes,shapes,frequencies,labels),1):
    z=np.r_[0,.45*np.array(shape),0]
    for wall in [-.09,4]:ax.add_patch(Rectangle((wall,-.85),.09,1.7,color='#b8c2cd'))
    ax.plot([0,4],[0,0],ls='--',lw=1,color='#929eac')
    ax.plot(x,z,color='#235b82',lw=2)
    ax.scatter(x[1:4],z[1:4],s=190,facecolor='#e3edf5',edgecolor='#235b82',zorder=3)
    for i in range(1,4):
        ax.text(i,z[i],str(i),ha='center',va='center',fontsize=9,zorder=4)
    ax.text(2,-1.1,label,ha='center',fontsize=12)
    ax.text(2,-1.46,freq,ha='center',fontsize=11)
    ax.set(xlim=(-.35,4.35),ylim=(-1.7,1.05),title=f'Mode {j}')
    ax.set_aspect('equal');ax.axis('off')
fig.suptitle('Three independent shapes of a string with three equal loads',fontsize=15,y=.96)
fig.text(.5,.07,'Fixed walls • dashed equilibrium line • common arbitrary displacement scale',ha='center',fontsize=11)
fig.text(.5,.02,'Each shape oscillates sinusoidally; joining segments show the instantaneous string profile.',ha='center',fontsize=10)
fig.subplots_adjust(left=.025,right=.98,top=.85,bottom=.17,wspace=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=145,facecolor='white')
plt.close(fig)
