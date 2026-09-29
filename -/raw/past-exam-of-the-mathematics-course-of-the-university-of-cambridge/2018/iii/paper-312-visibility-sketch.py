#!/usr/bin/env python3
"""Normalized schematic without reionization; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
eta=np.linspace(0,1,1200);width=.025;star=.28
s=1/(1+np.exp(-(eta-star)/width))
E=(s-s[0])/(s[-1]-s[0]);g=s*(1-s)/width/(s[-1]-s[0])
fig,axes=plt.subplots(1,2,figsize=(7,3.1),dpi=100)
for ax in axes:
    ax.set_xlim(0,1);ax.set_xticks([0,star,1],['early',r'$\eta_*$',r'$\eta_0$']);ax.set_xlabel('conformal time')
axes[0].plot(eta,E,color='#356fa8');axes[0].set_ylabel(r'$e^{-\tau}$');axes[0].set_ylim(-.04,1.05)
axes[1].plot(eta,g,color='#bf4c36');axes[1].fill_between(eta,0,g,alpha=.13,color='#bf4c36');axes[1].set_ylabel(r'$g= d e^{-\tau}/d\eta$');axes[1].set_ylim(0,11)
fig.tight_layout();fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'),facecolor='white')
