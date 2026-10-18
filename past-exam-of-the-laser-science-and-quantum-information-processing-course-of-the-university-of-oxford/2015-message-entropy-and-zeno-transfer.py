"""Original entropy and Zeno-transfer curves; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axs=plt.subplots(1,2,figsize=(12,4.7),layout='constrained',facecolor='white')
p=np.linspace(0,.5,501);z=2*p
h=np.ones_like(p);mask=(z>0)&(z<1);h[mask]-=z[mask]*np.log2(z[mask])+(1-z[mask])*np.log2(1-z[mask])
a=axs[0];a.plot(p,h,lw=2.5,color='#2563eb');a.scatter([.25],[2],color='#dc2626',zorder=4);a.annotate('2 bits: four equal probabilities',xy=(.25,2),xytext=(.065,1.72),arrowprops=dict(arrowstyle='->'),fontsize=10);a.set(xlabel=r'$p$ (with $q=1/2-p$)',ylabel='Shannon entropy (bits)',title='Four-message information',xlim=(0,.5),ylim=(.95,2.08));a.grid(alpha=.2)
n=np.arange(1,101);follow=np.cos(np.pi/(2*n))**(2*n);final=(1+np.cos(np.pi/n)**n)/2
b=axs[1];b.plot(n,follow,lw=2.3,label='All measurements follow branch',color='#2563eb');b.plot(n,final,lw=2,ls='--',label='Final target, all histories',color='#dc2626');b.axhline(1,color='#475569',lw=1);b.set(xlabel='Number of rotating measurements',ylabel='Probability',title=r'Known input $|0\rangle$ to target $|1\rangle$',xlim=(1,100),ylim=(-.02,1.03));b.legend(fontsize=9,loc='lower right');b.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
