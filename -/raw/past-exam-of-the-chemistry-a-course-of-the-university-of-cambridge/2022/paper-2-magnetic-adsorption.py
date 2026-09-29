"""Ideal magnetic Langmuir coverage; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

fig,axes=plt.subplots(1,2,figsize=(9,3.9),layout='constrained')
p=np.linspace(0,5,500)
for field,color in [(0,'#245c9f'),(1,'#b45309'),(2,'#37774b')]:
    b=np.cosh(field)
    axes[0].plot(p,b*p/(1+b*p),lw=2,color=color,label=f'$|x|={field}$')
axes[0].set(xlabel='$b(0)p$',ylabel='coverage $\\theta$',title='Isotherms at fixed temperature',xlim=(0,5),ylim=(0,1))
axes[0].legend(frameon=False,fontsize=10)
x=np.linspace(-4,4,500)
for load,color in [(.1,'#245c9f'),(1,'#b45309'),(5,'#37774b')]:
    y=load*np.cosh(x)
    axes[1].plot(x,y/(1+y),lw=2,color=color,label=f'$b(0)p={load:g}$')
axes[1].set(xlabel='$x=\\mu_{\\rm B}B/(k_{\\rm B}T)$',ylabel='coverage $\\theta$',
            title='Field dependence at fixed gas pressure',xlim=(-4,4),ylim=(0,1))
axes[1].legend(frameon=False,fontsize=10)
for ax in axes:
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.17)
fig.savefig(Path(__file__).stem+'.png',dpi=140,facecolor='white')
plt.close(fig)
