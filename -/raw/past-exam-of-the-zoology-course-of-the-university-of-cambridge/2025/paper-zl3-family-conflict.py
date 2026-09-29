"""Illustrative allocation model for NST II Zoology ZL3 2025 Q2.

Chosen functions only, not measurements; Python 3.14, numpy and matplotlib.
PNG output is written to the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 15, 600)
benefit = 6*np.log1p(x)
cost = x
relatedness = .5
fig, axes = plt.subplots(1, 2, figsize=(10, 4), facecolor='white')
axes[0].plot(x, benefit-cost, color='#2b688f', label=r'Parent: $B-C$')
axes[0].plot(x, benefit-relatedness*cost, color='#b7672d', label=r'Offspring: $B-rC$, $r=1/2$')
axes[0].scatter([5, 11], [6*np.log(6)-5, 6*np.log(12)-5.5], color=['#2b688f', '#b7672d'], zorder=4)
axes[0].set(xlabel='Investment x (arbitrary units)', ylabel='Objective (arbitrary units)', title='Different allocation optima')
axes[0].legend(frameon=False, fontsize=9, loc='lower right')
axes[1].plot(x, 6/(1+x), color='#276e5b', label=r"Marginal benefit $B'=6/(1+x)$")
axes[1].axhline(1, color='#2b688f', label=r"Parental cost $C'=1$")
axes[1].axhline(.5, color='#b7672d', label=r"Offspring-weighted cost $rC'=1/2$")
axes[1].set(xlabel='Investment x (arbitrary units)', ylabel='Marginal benefit or cost', ylim=(0, 2.4), title='Opposed interests for 5 < x < 11')
axes[1].legend(frameon=False, fontsize=8.5, loc='upper right')
for ax in axes:
    ax.axvspan(5, 11, color='#d3cfb8', alpha=.4)
    for xx in [5, 11]:ax.axvline(xx, color='#777777', ls='--', lw=.8)
    ax.set_xlim(0, 15)
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.15)
fig.text(.5, .012, 'Stipulated functions B(x) = 6 ln(1+x), C(x) = x; no signal costs or density effects included.', ha='center', fontsize=9)
fig.tight_layout(rect=(0,.06,1,1))
fig.savefig('paper-zl3-family-conflict.png', dpi=140, facecolor='white', bbox_inches='tight')
plt.close(fig)
