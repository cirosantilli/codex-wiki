#!/usr/bin/env python3
"""Render symmetric magnetic-bending equilibria to a PNG in the current directory."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

height = np.linspace(0, 1, 500)
fig, axes = plt.subplots(1, 2, figsize=(8.5, 4.3), dpi=100, facecolor='white')
for ax, kh, title in zip(axes, (1.0, 2.2), ('Stable magnetic modes', 'A growing magnetic mode')):
    profile = np.sin(kh * height) / np.sin(kh)
    assert np.isclose(profile[0], 0) and np.isclose(profile[-1], 1)
    ax.set_facecolor('white')
    ax.plot(height, profile, color='#256389', lw=2.3)
    ax.axhline(1, color='#777', ls='--', lw=0.8)
    if kh > np.pi / 2:
        peak_height = np.pi / (2 * kh)
        peak = 1 / np.sin(kh)
        ax.scatter([peak_height], [peak], color='#ad4936', s=32, zorder=3)
        ax.annotate('Interior maximum', xy=(peak_height, peak), xytext=(0.20, 1.37),
                    fontsize=10, arrowprops={'arrowstyle': '->', 'color': '#ad4936'})
    ax.set_title(title + '\n' + rf'$KH={kh}$', fontsize=12)
    ax.set_xlabel(r'Height $z/H$', fontsize=11)
    ax.set_ylabel(r'Radial field $B_x/B_+$', fontsize=11)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.5)
    ax.grid(alpha=0.16)
fig.subplots_adjust(left=0.09, right=0.97, bottom=0.15, top=0.82, wspace=0.35)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white')
plt.close(fig)
