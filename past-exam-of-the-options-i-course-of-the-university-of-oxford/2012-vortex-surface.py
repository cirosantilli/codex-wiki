"""Python 3.14; numpy and matplotlib. Write the PNG in the current directory."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
r=np.linspace(0,4,1200)
z=np.empty_like(r);core=r<=1
z[core]=-(2-r[core]**2)/2;z[~core]=-1/(2*r[~core]**2)
fig,ax=plt.subplots(figsize=(7,3.6),layout='constrained',facecolor='white')
ax.axhline(0,color='gray',ls=':',lw=1,label='Far-field level')
ax.plot(r[core],z[core],color='#b34c37',lw=2.5,label='Rotating core')
ax.plot(r[~core],z[~core],color='#246b93',lw=2.5,label='Irrotational exterior')
ax.axvline(1,color='#777777',ls='--',lw=1)
ax.scatter([0,1],[-1,-.5],color='#333333',s=22,zorder=3)
ax.annotate('Core edge',xy=(1,-.5),xytext=(1.5,-.65),arrowprops={'arrowstyle':'->'},fontsize=10)
ax.set(xlabel=r'Radius $r/a$',ylabel=r'Height $(z-C)ga^2/\Gamma^2$',title='Vortex free surface',xlim=(0,4),ylim=(-1.08,.09))
ax.legend(frameon=False,loc='lower right');ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd()/'2012-vortex-surface.png',dpi=150,facecolor='white')
