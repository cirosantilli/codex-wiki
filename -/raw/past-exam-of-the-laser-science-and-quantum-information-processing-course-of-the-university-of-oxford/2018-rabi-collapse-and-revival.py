"""Original ideal Jaynes-Cummings inversion; Python 3.14, NumPy/Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':12,'axes.spines.top':False,'axes.spines.right':False})
nbar=25.;n=np.arange(121)
p=np.zeros(len(n));p[0]=np.exp(-nbar)
for j in range(1,len(n)):p[j]=p[j-1]*nbar/j
t=np.linspace(0,42,10001)
inversion=p@np.cos(2*np.sqrt(n[:,None]+1)*t[None,:])
fig,ax=plt.subplots(figsize=(9,4.1),layout='constrained',facecolor='white')
ax.plot(t,inversion,color='#2a699c',lw=1)
revival=2*np.pi*np.sqrt(nbar)
ax.axvline(revival,color='#9a4b35',ls='--',lw=1)
ax.text(revival+.5,.87,r'$t_{\rm rev}\simeq2\pi\sqrt{\bar n}/g$',fontsize=11)
ax.text(4,.78,'Collapse',ha='center')
ax.set(xlabel=r'Time $gt$',ylabel=r'Atomic inversion $\langle\sigma_z\rangle$',title=r'Coherent initial field: $\bar n=25$; atom initially excited',xlim=(0,42),ylim=(-1.1,1.15))
ax.grid(alpha=.18)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=120,facecolor='white',transparent=False)
