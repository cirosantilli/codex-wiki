from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
plt.rcParams.update({"font.size":11,"font.family":"DejaVu Sans","figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})

fig,axs=plt.subplots(1,2,figsize=(11.7,5.1),layout='constrained')
ax=axs[0];ax.axvline(0,color='black',lw=2);ax.axvline(5,color='black',lw=2)
for n,E in [(1,.075206),(2,.300824),(3,.676854)]:ax.hlines(E,0,5,color='#174c75',lw=1.7);ax.text(2.5,E+.014,f'n={n}: {1000*E:.0f} meV',ha='center',fontsize=11)
ax.text(2.5,-.08,'Each carrier mass = 0.2 electron mass',ha='center',fontsize=10)
ax.set(xlim=(-.6,5.6),ylim=(-.13,.78),xlabel='Well coordinate (nm)',ylabel='Energy above its band edge (eV)',title='Explicit infinite-barrier estimate')
ax=axs[1];E=np.linspace(1.6,2.4,1400);edges=[1.770412,2.221648];spectrum=np.zeros_like(E)
for edge in edges:spectrum+=np.where(E>edge,.45,0)+.8/(1+((E-(edge-.025))/.004)**2)
spectrum+=np.where(E>2.3,.3,0);ax.plot(E,spectrum,color='#174c75',lw=1.8)
for edge in edges:ax.axvline(edge,color='#b35b15',ls=':',lw=1)
ax.axvline(2.3,color='gray',ls='--');ax.text(2.32,1.48,'barrier\nabsorption',fontsize=9,ha='center');ax.set(xlim=(1.6,2.4),ylim=(0,1.65),xlabel='Photon energy (eV)',ylabel='Relative absorption (schematic)',title='Illustrative 4.2 K spectrum')
fig.suptitle('5 nm quantum well: subband thresholds plus enhanced excitons',fontsize=15)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=140,transparent=False)
