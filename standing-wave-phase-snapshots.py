"""Original phase snapshots of two waves and their fixed-end standing sum.

Run from _media; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 1.0, 1201)
nodes = np.arange(4) / 3
phases = [0.0, np.pi / 4, np.pi / 2, np.pi]
labels = [r'$t=0$', r'$t=1/240\ \mathrm{s}$', r'$t=1/120\ \mathrm{s}$', r'$t=1/60\ \mathrm{s}$']
fig, axes = plt.subplots(4, 1, figsize=(9.6, 8.0), sharex=True, facecolor='white')
for ax, phase, label in zip(axes, phases, labels, strict=True):
    right = 0.5 * np.sin(3 * np.pi * x - phase)
    left = 0.5 * np.sin(3 * np.pi * x + phase)
    total = right + left
    envelope = np.abs(np.sin(3 * np.pi * x))
    ax.set_facecolor('white')
    ax.plot(x, envelope, color='#b8bec7', lw=1, ls=':')
    ax.plot(x, -envelope, color='#b8bec7', lw=1, ls=':')
    ax.axhline(0, color='#aaa', lw=0.7)
    for node in nodes:
        ax.axvline(node, color='#d7dce1', lw=1)
    ax.plot(x, right, color='#ca6d16', lw=1.6, ls='--', label='Right-moving constituent')
    ax.plot(x, left, color='#178451', lw=1.6, ls='-.', label='Left-moving constituent')
    ax.plot(x, total, color='#245cb3', lw=2.8, label='Standing sum')
    ax.scatter(nodes, np.zeros(4), color='#222', s=28, zorder=6)
    ax.text(0.015, 0.94, label, transform=ax.transAxes, va='top', fontsize=12,
            bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
    ax.set_ylim(-1.2, 1.2)
    ax.set_xlim(-0.02, 1.02)
    ax.set_yticks([-1, 0, 1])
    ax.set_ylabel(r'$y/(2a)$', fontsize=12)
    ax.spines[['top', 'right']].set_visible(False)
    if np.isclose(phase, np.pi / 2):
        for xp, direction in [(1/6, -1), (1/2, 1), (5/6, -1)]:
            ax.annotate('', xy=(xp, direction * 0.66), xytext=(xp, 0),
                        arrowprops={'arrowstyle': '->', 'color': '#245cb3', 'lw': 2})
        ax.text(0.98, 0.97, 'Straight now; arrows show material velocity',
                ha='right', va='top', transform=ax.transAxes, fontsize=10,
                bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
axes[-1].set_xticks(nodes, ['0', '1/3', '2/3', '1'])
axes[-1].set_xlabel(r'Position $x$ (m)', fontsize=12)
fig.suptitle('Two moving waves, one stationary nodal pattern', fontsize=17, y=0.985)
fig.text(0.5, 0.944, r'Constructed third mode: $L=1$ m, $c=20$ m/s, $f=30$ Hz; black dots are permanent nodes',
         ha='center', fontsize=10.5)
handles, legend_labels = axes[0].get_legend_handles_labels()
fig.legend(handles, legend_labels, loc='lower center', bbox_to_anchor=(0.5, 0.005),
           ncol=3, frameon=False, fontsize=10)
fig.subplots_adjust(left=0.09, right=0.975, top=0.905, bottom=0.10, hspace=0.22)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
