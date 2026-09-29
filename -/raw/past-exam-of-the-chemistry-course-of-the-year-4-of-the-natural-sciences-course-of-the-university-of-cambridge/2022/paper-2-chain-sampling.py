"""Original explanatory figure. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run through the root Makefile; the PNG basename is written to the current directory.
"""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
from tools.chemistry_diagram import bond, atom, ring, wedge, curly, flow, finish, save
plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axs=plt.subplots(5,2,figsize=(11,10),layout='constrained');rng=np.random.default_rng(22231)
labels=['Hard core, low T: expanded','Hard core, room T: similar coil','LJ, low T, short run: trapped','LJ, low T, equilibrated: compact','LJ, high T, equilibrated: expanded'];means=[4.1,4.25,5.4,2.1,4.4];width=[.6,.7,.15,.4,.85]
for row,(lab,mu,sd) in enumerate(zip(labels,means,width)):
 n=700;z=np.zeros(n);z[0]=mu
 for i in range(1,n):z[i]=mu+.93*(z[i-1]-mu)+sd*np.sqrt(1-.93**2)*rng.normal()
 z=np.clip(z,.15,8.8);a=axs[row,0];a.plot(z,lw=.8);a.set(ylabel=r'$d/\sigma$',ylim=(0,9),title=lab);a=axs[row,1];a.hist(z,bins=22,density=True,color='#245c9f',alpha=.75);a.set(xlim=(0,9),ylabel='Normalized frequency')
axs[-1,0].set_xlabel('Sweep index (illustrative)');axs[-1,1].set_xlabel(r'$d/\sigma$');fig.suptitle('Qualitative traces and histograms; seeded illustrations, not computed polymer ensembles',fontsize=12)
save(fig,'paper-2-chain-sampling.png')
