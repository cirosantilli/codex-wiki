#!/usr/bin/env python3
"""Odd finite-well matching curves; Python 3.14, NumPy/Matplotlib.
Outputs a white-background PNG in the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(7.4,4.9),layout='constrained',facecolor='white')
ax.set_facecolor('white')
x=np.linspace(.002,np.pi/2-.002,400);ax.plot(x,-x/np.tan(x),ls='--',color='0.6',lw=1.5,label=r'Negative branch: excluded by $\eta>0$')
x=np.linspace(np.pi/2+.002,np.pi-.002,600);ax.plot(x,-x/np.tan(x),color='#2466a4',lw=2.3,label=r'$\eta=-\xi\cot\xi$')
for R,col in [(1.2,'#d19431'),(2.3,'#338451')]:
 x=np.linspace(0,R,500);ax.plot(x,np.sqrt(np.maximum(0,R*R-x*x)),color=col,lw=2,label=f'Circle radius R={R}')
lo,hi=np.pi/2,2.3
for _ in range(50):
 mid=(lo+hi)/2
 if -mid/np.tan(mid)<np.sqrt(2.3**2-mid**2):lo=mid
 else:hi=mid
root=(lo+hi)/2;ax.scatter([root],[-root/np.tan(root)],color='#338451',s=33,zorder=5)
ax.axhline(0,color='0.25',lw=.8);ax.axvline(np.pi/2,color='0.55',ls=':',lw=1)
ax.set(xlim=(0,np.pi),ylim=(-1.15,3.6),xlabel=r'$\xi=ka$',ylabel=r'$\eta=\kappa a$',title='Odd-parity bound states in a finite square well')
ax.set_xticks([0,np.pi/2,np.pi],[r'$0$',r'$\pi/2$',r'$\pi$']);ax.grid(alpha=.15);ax.legend(loc='upper left',fontsize=9,facecolor='white')
fig.savefig(Path.cwd()/'2010-odd-well-bound-states.png',dpi=165,facecolor='white')
