"""Original teaching plot. Python 3.14; NumPy 2.3.5, Matplotlib 3.10.7. Writes PNG basename to cwd."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
plt.rcParams.update({"font.size":11,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,(a,b)=plt.subplots(1,2,figsize=(10.3,4.0),layout='constrained',gridspec_kw={'width_ratios':[1.12,1]})
j=np.arange(13);u=.37*np.cos(2*np.pi*j/6)
a.axhline(0,color='.75',lw=1);a.scatter(j,np.zeros_like(j),s=17,facecolor='white',edgecolor='.65')
a.plot(j,u,color='#1b638d',lw=1.4);a.scatter(j,u,s=65,color='#1b638d',zorder=3)
for z,v in zip(j,u):a.plot([z,z],[0,v],color='.5',lw=.8)
a.set(xlabel='Site index',ylabel='Illustrative displacement',title='A quantized normal-mode coordinate',ylim=(-.65,.65));a.set_yticks([-.4,0,.4]);a.grid(alpha=.12)
x=np.linspace(-np.pi,np.pi,600)
b.plot(x,2*np.abs(np.sin(x/2)),lw=2.5,label='Lattice dispersion')
b.plot(x,np.abs(x),'--',color='.5',label='Acoustic approximation')
b.set(xlim=(-np.pi,np.pi),ylim=(0,3.3),xlabel=r'$ka$',ylabel=r'$\omega/\sqrt{K/m_0}$',title='One monatomic acoustic branch')
b.set_xticks([-np.pi,0,np.pi],[r'$-\pi$','0',r'$\pi$']);b.legend(loc='upper center',fontsize=9);b.grid(alpha=.15)
fig.savefig(Path(__file__).stem+'.png',dpi=150,facecolor='white');plt.close(fig)
