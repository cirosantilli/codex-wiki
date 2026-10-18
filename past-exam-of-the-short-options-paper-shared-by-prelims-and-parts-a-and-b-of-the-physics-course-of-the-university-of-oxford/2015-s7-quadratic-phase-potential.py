"""Original cosine-of-square potential and its harmonic frequencies. PNG to CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig,axes=plt.subplots(1,2,figsize=(9,3.8),layout='constrained')
x=np.linspace(-2.12,2.12,2500)
ax=axes[0];ax.plot(x,np.cos(np.pi*x*x),color='#1769aa')
stable=np.array([-np.sqrt(3),-1,1,np.sqrt(3)])
unstable=np.array([-2,-np.sqrt(2),0,np.sqrt(2),2])
ax.scatter(stable,-np.ones_like(stable),color='#168347',label='stable minima',zorder=4)
ax.scatter(unstable,np.ones_like(unstable),facecolor='white',edgecolor='#b64f28',label='unstable maxima',zorder=4)
ax.annotate('quartically flat maximum',(0,1),xytext=(-.85,.35),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set(title=r'$V(x)=V_0\cos[\pi(x/l_0)^2]$, $V_0>0$',xlabel=r'$x/l_0$',ylabel=r'$V/V_0$',ylim=(-1.25,1.3))
ax.legend(loc='lower center',ncols=2,fontsize=8)
ax=axes[1];n=np.arange(1,10,2)
ax.scatter(n,np.sqrt(n),color='#168347',s=40)
ax.set(title='Harmonic frequencies at the stable minima',xlabel='Odd equilibrium index n',ylabel=r'$\omega_n l_0/(2\pi\sqrt{V_0/m})$',xticks=n,xlim=(.5,9.5),ylim=(0,3.4))
ax.text(4,.6,r'$\omega_n\ \propto\ \sqrt{n}$',fontsize=12)
for ax in axes:ax.grid(alpha=.18)
fig.savefig(Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white')
plt.close(fig)
