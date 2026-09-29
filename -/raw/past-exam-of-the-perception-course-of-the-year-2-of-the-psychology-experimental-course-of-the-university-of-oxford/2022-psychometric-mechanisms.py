#!/usr/bin/env python3
"""Original theoretical illustration, not participant data.
Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7; outputs PNG to CWD.
Dependencies are pinned in the repository pyproject.toml.
"""
from pathlib import Path
from math import erf,sqrt
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(8.2,3.6),layout='constrained')
x=np.linspace(-4,4,801)
phi=lambda v:np.array([.5*(1+erf(float(z)/sqrt(2))) for z in v])
pdf=lambda v:np.exp(-v*v/2)/sqrt(2*np.pi)
ax.plot(x,pdf(x),color='#2166ac',lw=2,label='Response at mean stimulus μ = 0')
ax.plot(x,pdf(x-1.5),color='#b2182b',lw=2,label='Response at mean stimulus μ = 1.5')
ax.axvline(.5,color='black',ls='--',lw=1)
sel=x>=.5
ax.fill_between(x[sel],pdf(x[sel]-1.5),alpha=.18,color='#b2182b')
ax.text(.65,.30,'Respond yes\nabove criterion',fontsize=9)
ax.set(xlabel='Noisy internal response',ylabel='Probability density',title='A decision samples a distribution tail',xlim=(-4,4),ylim=(0,.44))
ax.legend(loc='upper left',fontsize=7,frameon=False)
bx.plot(x,phi(x),color='#2166ac',lw=2,label='Yes probability: Φ(x)')
bx.plot(x,.5+.5*phi(x),color='#b2182b',lw=2,label='2AFC correct: 0.5 + 0.5 Φ(x)')
bx.plot(x,.5+.46*phi(x),color='#5b3c88',lw=2,ls='--',label='2AFC, upper error asymptote 0.04')
bx.scatter([0],[.73],s=25,color='#5b3c88',zorder=5)
bx.axhline(.5,color='grey',lw=.6)
bx.axhline(.96,color='grey',lw=.6,ls=':')
bx.set(xlabel='Standardized stimulus coordinate x',ylabel='Response probability',title='Chance and lapses alter the fitted curve',xlim=(-4,4),ylim=(0,1.02))
bx.legend(loc='lower right',fontsize=7,frameon=False)
bx.grid(alpha=.16)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'),dpi=120,transparent=False,metadata={'Software':'Original probability calculations; no experimental data'})
plt.close(fig)
