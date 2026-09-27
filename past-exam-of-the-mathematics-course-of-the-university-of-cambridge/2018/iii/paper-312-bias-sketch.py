#!/usr/bin/env python3
"""Schematic deterministic bias power ratio; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
k=np.geomspace(.2,20,1500)
fig,ax=plt.subplots(figsize=(7,3.6),dpi=100)
ax.plot(k,(1+1/k**2)**2,label=r'$f_{\rm NL}>0$',color='#bf4c36')
ax.plot(k,(1-1/k**2)**2,label=r'$f_{\rm NL}<0$',color='#356fa8')
ax.axhline(1,color='.3',ls='--',label='Gaussian')
ax.scatter([1],[0],color='#356fa8',zorder=4)
ax.annotate('bias changes sign',xy=(1,0),xytext=(1.7,.12),arrowprops={'arrowstyle':'->'},fontsize=9)
ax.set_xscale('log');ax.set_yscale('symlog',linthresh=.05)
ax.set_xlabel(r'$k/k_{\rm cancel}$ (smaller $k$ = larger scale)')
ax.set_ylabel(r'$P_g/(b_{10}^2 P_m)$')
ax.set_ylim(-.005,1000);ax.set_xlim(.2,20)
ax.legend(loc='upper right',fontsize=9)
fig.tight_layout();fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),facecolor='white')
