import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
plt.rcParams.update({'font.size':11,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','savefig.facecolor':'white'})

k=1.380649e-23/1.602176634e-19;gap=.04;deg=9*np.exp(gap/(k*150));t90=gap/(k*np.log(9*deg))
def bound(T):return 1/(1+deg*np.exp(-gap/(k*np.asarray(T))))
fig,ax=plt.subplots(1,2,figsize=(10,3.7),layout='constrained');T=np.linspace(.1,260,1000);ax[0].plot(T,bound(T));ax[0].plot([t90,150],[.9,.1],'o');ax[0].annotate(f'{t90:.1f} K, 0.9',xy=(t90,.9),xytext=(85,.86),arrowprops={'arrowstyle':'->'},fontsize=9);ax[0].annotate('150 K, 0.1',xy=(150,.1),xytext=(155,.35),arrowprops={'arrowstyle':'->'},fontsize=9);ax[0].set(xlabel='Temperature (K)',ylabel='Bound-state probability',title='The two model occupancy points',ylim=(-.03,1.05))
T=np.geomspace(1,1e5,1200);ax[1].semilogx(T,bound(T));ax[1].axhline(1/(1+deg),color='crimson',ls='--',label=r'$1/(1+g)$');ax[1].set(xlabel='Temperature (K), logarithmic scale',ylabel='Bound-state probability',title='Finite-degeneracy high-temperature limit',ylim=(-.03,1.05));ax[1].legend(fontsize=9)
fig.suptitle(f'Original two-level calculation: gap 0.04 eV; effective g = {deg:.2f}; no spin factor',fontsize=11)
fig.savefig('paper-1-donor-occupancy.png',dpi=155)
