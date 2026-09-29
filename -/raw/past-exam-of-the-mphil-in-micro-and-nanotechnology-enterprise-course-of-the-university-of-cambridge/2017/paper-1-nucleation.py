"""Original explanatory diagram; run in the desired output directory. Tested with Python 3.14, numpy and matplotlib."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, FancyArrowPatch
plt.rcParams.update({"font.size":10,"figure.facecolor":"white","axes.facecolor":"white","savefig.facecolor":"white"})
fig,axs=plt.subplots(1,2,figsize=(10,3.8),layout='constrained')
a=axs[0];r=np.linspace(0,2.1,500);a.plot(r,3*r*r-2*r**3,lw=2,color='#246b98',label=r'$\Delta G/\Delta G_*$');a.plot(r,3*r*r,ls='--',color='#bd7839',label='surface cost');a.plot(r,-2*r**3,ls=':',color='#75539c',label='bulk gain');a.axvline(1,ls='--',color='#aaa');a.plot(1,1,'ko');a.text(1.05,1.25,'critical nucleus');a.set(xlim=(0,2.1),ylim=(-4,4),xlabel=r'$r/r_*$',ylabel='Normalized free energy',title='Volume gain competes with interface cost');a.legend(fontsize=8,loc='lower left')
a=axs[1];t=np.linspace(0,10,600);c=np.where(t<3,.3+.55*t,np.where(t<4.2,1.95-.6*(t-3),.4+.83*np.exp(-(t-4.2)/2)))
a.plot(t,c,color='#246b98',lw=2);a.axhline(.4,color='#998538',ls='--');a.axhline(1.65,color='#b35332',ls='--');a.text(9.8,.44,r'$C_s$: solubility',ha='right',fontsize=9);a.text(9.8,1.69,r'$C_n$: nucleation threshold',ha='right',fontsize=9)
mask=c>1.65;a.fill_between(t,0,2.2,where=mask,color='#e8a77e',alpha=.3);a.annotate('short birth interval',(3.1,1.9),(4.8,2.08),ha='center',fontsize=9,arrowprops={'arrowstyle':'->'});a.text(1.1,.25,'buildup');a.text(5.4,.85,'growth of existing seeds');a.set(xlim=(0,10),ylim=(0,2.3),xlabel='Time (arbitrary units)',ylabel='Growth-species concentration',title='La Mer scheme: separate birth and growth')
fig.savefig('paper-1-nucleation.png',dpi=160);plt.close(fig)
