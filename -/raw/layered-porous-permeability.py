"""Compare normal and parallel flow through two layers; save PNG to cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: python ../layered-porous-permeability.py
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

permeabilities = np.array([1.0, 9.0])
fractions = np.array([0.5, 0.5])
normal = 1 / np.sum(fractions / permeabilities)
parallel = np.sum(fractions * permeabilities)
resistance_shares = (fractions / permeabilities) / np.sum(fractions / permeabilities)
flow_shares = fractions * permeabilities / parallel
blue, orange, ink = '#166a9c', '#b14d25', '#273c48'
colors = ['#fbe5c8', '#d8eaf5']
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, axes = plt.subplots(2, 2, figsize=(9.2, 6.4), dpi=120, gridspec_kw={'height_ratios': [1.15, 1]})
fig.subplots_adjust(left=0.1, right=0.95, top=0.82, bottom=0.17, hspace=0.5, wspace=0.4)
fig.suptitle('Layer geometry changes bulk permeability', fontsize=18, y=0.97)
fig.text(0.5, 0.90, r'Equal thicknesses: $k_1=k_0$, $k_2=9k_0$; $k_0=10^{-12}\ \mathrm{m^2}$', ha='center', fontsize=12)
for col, title in enumerate(['Across layers: same discharge', 'Along layers: same head gradient']):
    ax = axes[0, col]
    ax.set(xlim=(-0.25, 1.25), ylim=(-0.2, 1.3))
    ax.axis('off')
    ax.set_title(title, fontsize=12, pad=10)
    for y, color in zip([0.5, 0], colors):
        ax.add_patch(Rectangle((0, y), 1, 0.5, fc=color, ec=ink, lw=1.3))
    if col == 0:
        ax.text(0.13, 0.75, 'k₁ = k₀', va='center')
        ax.text(0.13, 0.25, 'k₂ = 9k₀', va='center')
        for a, b in [(1.18, 0.54), (0.48, -0.13)]:
            ax.annotate('', xy=(0.75, b), xytext=(0.75, a), arrowprops={'arrowstyle': '-|>', 'color': blue, 'lw': 2.4, 'mutation_scale': 16})
        ax.text(-0.03, 1.13, 'High head', ha='left', fontsize=10)
        ax.text(-0.03, -0.15, 'Low head', ha='left', fontsize=10)
    else:
        for y, width in [(0.75, 1.2), (0.25, 3.5)]:
            ax.annotate('', xy=(1.17, y), xytext=(-0.15, y), arrowprops={'arrowstyle': '-|>', 'color': blue, 'lw': width, 'mutation_scale': 17})
        ax.text(0.5, 0.91, 'k₁ = k₀: 10% of total Q', ha='center', fontsize=10)
        ax.text(0.5, 0.42, 'k₂ = 9k₀: 90% of total Q', ha='center', fontsize=10)
        ax.text(-0.2, 1.13, 'High head', ha='left', fontsize=10)
        ax.text(1.22, 1.13, 'Low head', ha='right', fontsize=10)
head = axes[1, 0]
head.plot([0, 0.5, 1], [1, 1-resistance_shares[0], 0], color=orange, lw=2.6, marker='o')
head.axvline(0.5, color=ink, lw=1, ls='--')
head.set(xlim=(0, 1), ylim=(0, 1.1), xlabel='Fraction of depth along flow', ylabel='Normalized hydraulic head', title=f'Harmonic mean: k⊥ = {normal:g} k₀')
head.text(0.13, 0.3, '90% of head drop\nin the k₀ layer', color=orange, fontsize=10)
head.grid(alpha=0.15)
profile = axes[1, 1]
x = np.linspace(0, 1, 101)
profile.plot(x, 1-x, color=blue, lw=3.8, label='Layer 2 (9k₀)')
profile.plot(x, 1-x, color=orange, lw=1.6, ls='--', label='Layer 1 (k₀)')
profile.set(xlim=(0, 1), ylim=(0, 1.1), xlabel='Fraction of horizontal length', ylabel='Normalized hydraulic head', title=f'Arithmetic mean: k∥ = {parallel:g} k₀')
profile.legend(fontsize=9, loc='upper right')
profile.grid(alpha=0.15)
fig.text(0.5, 0.075, f'For the same head gradient: q∥/q⊥ = {parallel:g}/{normal:g} ≈ {parallel/normal:.2f}', ha='center', fontsize=12)
fig.text(0.5, 0.025, 'One fluid, full saturation, isotropic layers, perfect contact; head includes gravity.', ha='center', fontsize=10)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
plt.close(fig)
