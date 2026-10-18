"""Generic quantum-Hall schematic; no missing sample data reconstructed."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,2,figsize=(11,4.1),layout='constrained',facecolor='white')
a=axes[0];nu=np.linspace(1,6,1500);r=np.zeros_like(nu)
for v in np.arange(1.5,6,.999999):r+=np.exp(-((nu-v)/.13)**2)
a.plot(nu,r,color='#355a9b',lw=2);a.set(xlim=(6,1),ylim=(0,1.4),xlabel='nominal filling ν (field increases →)',ylabel='schematic ρxx, uncalibrated',title='A  Minima near integer filling')
for v in range(1,7):a.text(v,.07,str(v),ha='center',fontsize=9)
a.text(5.9,1.2,'Generic resolved-level limit; not the lost 0–12 T data',fontsize=9)
a=axes[1];E=np.linspace(0,4,1200);g=np.zeros_like(E);centres=[.5,1.5,2.5,3.5]
for c in centres:g+=np.exp(-((E-c)/.22)**2)
a.plot(E,g,color='#355a9b',lw=2);a.fill_between(E,0,g,color='#dce9f3')
for c in centres:
 mask=abs(E-c)<.065;a.fill_between(E,0,g,where=mask,color='#bd7820')
a.axvline(2,color='#269572',ls='--',label='μ in localized region');a.axvline(2.5,color='#8b5292',ls=':',label='μ at extended centre')
a.set(xlabel='energy / cyclotron spacing',ylabel='schematic density of states',ylim=(0,1.4),title='B  Localized tails, extended centres');a.legend(frameon=False,fontsize=9,loc='upper left')
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=110,facecolor='white')
