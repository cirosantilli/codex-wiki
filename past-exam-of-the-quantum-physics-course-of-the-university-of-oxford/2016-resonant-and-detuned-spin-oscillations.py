from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

tau=np.linspace(0,3*np.pi,1400)
plt.rcParams.update({'font.size':12})
fig, axes=plt.subplots(2,1,figsize=(8.4,5.6),sharex=True,sharey=True,layout='constrained',facecolor='white')
for ax,r,label,color in zip(axes,[0,1],['Resonance: half-detuning = 0','Detuned: half-detuning = drive coupling'],['#1261a0','#bd4e15']):
 p=np.sin(np.sqrt(1+r*r)*tau)**2/(1+r*r)
 ax.plot(tau,p,lw=2.3,color=color)
 ax.axhline(1/(1+r*r),ls=':',color=color,lw=1)
 ax.set(ylabel=r'$P_{\downarrow}(t)$',title=label,ylim=(-.04,1.08),xlim=(0,tau[-1]))
 ax.grid(alpha=.2); ax.set_facecolor('white')
axes[-1].set_xlabel(r'Dimensionless time $|\gamma|t$')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white',transparent=False)
