"""Original standard-solid plot; Python 3.14, NumPy 2.3, Matplotlib 3.10.
Output is always Path.cwd()/the script basename with suffix .png.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':11,'figure.facecolor':'white'})
x=np.logspace(-3,3,600)
g0,g1=1.,4.
gl=g0*g1/(g0+g1);gh=g1;dg=gh-gl
storage=gl+dg*x*x/(1+x*x)
loss=dg*x/(1+x*x)
fig,ax=plt.subplots(figsize=(7,4.4),layout='constrained')
ax.loglog(x,storage,color='#246b9a',lw=2.3,label=r"$G'$ (storage)")
ax.loglog(x,loss,color='#b54d38',lw=2.3,label=r"$G''$ (loss)")
ax.axhline(gl,color='#246b9a',ls='--',alpha=.5)
ax.axhline(gh,color='#246b9a',ls='--',alpha=.5)
ax.axvline(1,color='0.5',ls=':',lw=1)
ax.text(220,gl*1.12,r'$G_L$',color='#246b9a')
ax.text(220,gh*1.12,r'$G_H$',color='#246b9a')
ax.text(.011,.054,'slope +1',rotation=31,color='#b54d38')
ax.text(16,.17,'slope −1',rotation=-31,color='#b54d38')
ax.plot(1,dg/2,'o',color='#b54d38',ms=5)
ax.annotate('loss maximum',xy=(1,dg/2),xytext=(2.6,.53),arrowprops={'arrowstyle':'->','color':'0.4'},fontsize=10)
ax.set(xlim=(1e-3,1e3),ylim=(.002,8),xlabel=r'Reduced frequency $\omega\tau$',ylabel='Modulus (arbitrary consistent units)',title='One relaxation mode: two elastic plateaus')
ax.legend(loc='lower center',frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white')
plt.close(fig)
