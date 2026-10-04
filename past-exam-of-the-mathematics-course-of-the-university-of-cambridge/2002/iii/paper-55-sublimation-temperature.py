"""Original absorbed-radiation temperature sketches, writing basename to CWD.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; caller MPLCONFIGDIR respected.
"""
from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
S=5.;x=np.linspace(0,15,750)
fig,ax=plt.subplots(figsize=(7.5,4),dpi=120,facecolor='white');ax.set_facecolor('white')
for r,color,style,label in [(.2,'#1e609b','-','Cooler heating: r = 0.2'),(1.,'#b34535','--','Stronger heating: r = 1 (all-solid prediction)')]:
    theta=((1+(S+1)*x)*np.exp(-x) if r==1 else (r*(S+1)*np.exp(-x)-(r*S+1)*np.exp(-r*x))/(r-1))
    peak=S/(S+1) if r==1 else math.log((r*S+1)/(S+1))/(r-1)
    peakT=(1+(S+1)*peak)*math.exp(-peak) if r==1 else (r*(S+1)*math.exp(-peak)-(r*S+1)*math.exp(-r*peak))/(r-1)
    ax.plot(x,theta,style,color=color,lw=2,label=label)
    ax.scatter([peak],[peakT],s=28,color=color,zorder=4)
ax.axhline(1,color='#6a6a6a',lw=.9,ls=':',label=r'Sublimation surface: $T_s$')
ax.axhline(2.4,color='#538642',lw=1.2,ls='-.',label=r'Illustrative melting level: $T_m$')
ax.annotate('Subsurface maximum reaches melting',xy=(5/6,6*math.exp(-5/6)),xytext=(3,2.75),arrowprops={'arrowstyle':'->','color':'#b34535'},fontsize=9,color='#b34535')
ax.set(xlabel=r'Depth $\lambda z$',ylabel=r'$(T-T_\infty)/(T_s-T_\infty)$',xlim=(0,15),ylim=(0,3.05),title=r'Absorbed-radiation sublimation profile, $S=5$')
ax.grid(alpha=.18);ax.legend(frameon=False,fontsize=8,loc='upper right')
fig.tight_layout();fig.savefig(Path.cwd()/'paper-55-sublimation-temperature.png',facecolor='white',transparent=False);plt.close(fig)
