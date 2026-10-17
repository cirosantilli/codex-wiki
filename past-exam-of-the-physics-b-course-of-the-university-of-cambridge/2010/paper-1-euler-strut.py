import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

fig,ax=plt.subplots(1,2,figsize=(10,3.8),layout='constrained');x=np.linspace(0,1,600)
for n in [1,2,3]:ax[0].plot(x,np.sin(n*np.pi*x),label=fr'$n={n},\ P_n/P_1={n*n}$')
ax[0].plot([0,1],[0,0],'ko');ax[0].set(xlabel='Position / length',ylabel='Normalized lateral mode',title='Pinned ends: lowest mode buckles first');ax[0].legend(fontsize=9,loc='lower left')
a=np.linspace(-1,1,500)
for p in [.6,1,1.4]:ax[1].plot(a,(1-p)*a*a,label=fr'$P/P_{{cr}}={p}$')
ax[1].set(xlabel='Small mode amplitude (scaled)',ylabel='Quadratic potential (scaled)',title='Local straight-state stability');ax[1].legend(fontsize=9,loc='upper center');ax[1].text(-.96,-.4,'Quadratic only; no postbuckling branch inferred',fontsize=8)
fig.savefig('paper-1-euler-strut.png',dpi=155)
