"""Original chain dispersions and mode relaxation; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig,axs=plt.subplots(1,2,figsize=(12.5,4.7),layout='constrained',facecolor='white');x=np.linspace(0,1,600)
a=axs[0]
for ratio,col in [(0,'#2563eb'),(.25,'#7c3aed'),(1,'#dc2626')]:
 omega=2*np.sqrt(np.sin(np.pi*x/2)**2+ratio*np.sin(np.pi*x)**2);a.plot(x,omega,lw=2.3,color=col,label=f'G/K = {ratio:g}')
a.set(xlabel=r'Reduced wave number $ka/\pi$',ylabel=r'$\omega_0\sqrt{m/K}$',title='One monatomic acoustic branch',xlim=(0,1),ylim=(0,2.65));a.legend(fontsize=10,loc='lower right');a.grid(alpha=.2)
b=axs[1];t=np.linspace(0,15,1000)
for ratio,col in [(.2,'#2563eb'),(1,'#7c3aed'),(2,'#dc2626')]:
 if ratio<1:
  w=np.sqrt(1-ratio**2);u=np.exp(-ratio*t)*(np.cos(w*t)+ratio/w*np.sin(w*t))
 elif ratio==1:u=(1+t)*np.exp(-t)
 else:
  w=np.sqrt(ratio**2-1);u=(ratio+w)/(2*w)*np.exp(-(ratio-w)*t)-(ratio-w)/(2*w)*np.exp(-(ratio+w)*t)
 b.plot(t,u,color=col,lw=2.2,label=fr'$\gamma/\omega_0={ratio:g}$')
b.axhline(0,color='#94a3b8',lw=1);b.set(xlabel=r'Time $\omega_0t$',ylabel='Normalized mode displacement',title='Same initial displacement; zero initial velocity',xlim=(0,15),ylim=(-.65,1.1));b.legend(fontsize=10,loc='upper right');b.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,facecolor='white')
