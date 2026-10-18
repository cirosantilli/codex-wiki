"""Original axial S=3/2 level diagram; Python 3.14, numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 12, 'axes.spines.top': False, 'axes.spines.right': False})
h=6.62607015e-34
muB=9.2740100783e-24
nu=1e10
g=h*nu/(muB*.3)
D=.425*h*nu
B=np.linspace(0,.66,700)
fig,ax=plt.subplots(figsize=(8,5),layout='constrained')
colors=['#157f88','#aa3377','#4477aa','#cc7722']
for m,color in zip([-1.5,-.5,.5,1.5],colors):
    ax.plot(B,m*m+g*muB*B*m/D,color=color,label=rf'$m={m:g}$',lw=2)
for b,m,label in [(.045,.5,'0.045 T'),(.3,-.5,'0.300 T'),(.555,-1.5,'0.555 T')]:
    lo=m*m+g*muB*b*m/D
    hi=(m+1)**2+g*muB*b*(m+1)/D
    ax.annotate('',xy=(b,hi),xytext=(b,lo),arrowprops={'arrowstyle':'<->','color':'#111111','lw':1.7})
    ax.axvline(b,color='.65',ls=':',lw=1,zorder=0)
    ax.text(b+.008,(hi+lo)/2,label,rotation=90,ha='left',va='center',fontsize=10)
ax.set(xlabel='Applied axial field B (T)',ylabel='Energy / D',title='Axial spin 3/2: allowed resonances at 10 GHz',xlim=(0,.66),ylim=(-6.5,10.5))
ax.legend(ncol=2,loc='upper left',frameon=False)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name,dpi=150,facecolor='white',transparent=False)
