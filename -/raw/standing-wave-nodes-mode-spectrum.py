"""Original spatial amplitude and discrete mode spectrum of an ideal string.

Run from _media; tested with Python 3.14, matplotlib 3.10.7, numpy 2.3.5.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 1.0, 1201)
nodes = np.arange(4) / 3
antinodes = (2 * np.arange(3) + 1) / 6
n = np.arange(1, 7)
f = n * 10
fig, (spatial, spectrum) = plt.subplots(2, 1, figsize=(9.6, 6.4), facecolor='white')
spatial.plot(x, np.abs(np.sin(3 * np.pi * x)), color='#245cb3', lw=2.8,
             label='Oscillation amplitude / maximum amplitude')
spatial.scatter(nodes, np.zeros(4), color='#222', s=45, zorder=4, label='Nodes')
spatial.scatter(antinodes, np.ones(3), color='#ca6d16', s=45, zorder=4, label='Antinodes')
for xp in nodes:
    spatial.axvline(xp, color='#d9dde3', ls=':', lw=1)
spatial.annotate('', xy=(0, 0.28), xytext=(1/3, 0.28),
                 arrowprops={'arrowstyle': '<->', 'color': '#333', 'lw': 1.4})
spatial.text(1/6, 0.36, r'Node spacing $=\lambda/2=1/3$ m', ha='center', fontsize=10,
             bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
spatial.set_title(r'Third mode: three loops, four nodes, $\lambda=2/3$ m', loc='left', fontsize=13)
spatial.set_xlim(-0.02, 1.02)
spatial.set_ylim(-0.10, 1.18)
spatial.set_xticks(np.arange(7)/6, ['0', '1/6', '1/3', '1/2', '2/3', '5/6', '1'])
spatial.set_xlabel(r'Position $x$ (m)', fontsize=11)
spatial.set_ylabel(r'Amplitude $/(2a)$', fontsize=11)
spatial.legend(loc='upper center', bbox_to_anchor=(0.5, -0.23), ncol=3, frameon=False, fontsize=9)
colors = ['#879bb9' if i != 3 else '#245cb3' for i in n]
spectrum.vlines(f, 0, 1, colors=colors, linewidth=2.5)
spectrum.scatter(f, np.ones(6), c=colors, s=55, zorder=3)
for ni, fi in zip(n, f, strict=True):
    spectrum.text(fi, 1.12, f'n = {ni}', ha='center', fontsize=10)
spectrum.set_title(r'Allowed fixed-end frequencies: $f_n=nc/(2L)=10n$ Hz', loc='left', fontsize=13)
spectrum.set_xlim(0, 70)
spectrum.set_ylim(0, 1.4)
spectrum.set_xticks(np.arange(0, 71, 10))
spectrum.set_yticks([])
spectrum.set_xlabel(r'Frequency $f$ (Hz)', fontsize=11)
spectrum.text(0.98, 0.24, 'Line heights only mark allowed frequencies;\nthey do not represent measured amplitudes.',
              transform=spectrum.transAxes, ha='right', fontsize=10,
              bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
for ax in (spatial, spectrum):
    ax.set_facecolor('white')
    ax.spines[['top', 'right']].set_visible(False)
spectrum.spines['left'].set_visible(False)
fig.suptitle('Spatial nodes and the discrete mode spectrum', fontsize=17, y=0.99)
fig.text(0.5, 0.94, r'Constructed uniform fixed-end string: $L=1$ m, $c=20$ m/s', ha='center', fontsize=11)
fig.subplots_adjust(left=0.095, right=0.975, top=0.86, bottom=0.10, hspace=0.76)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
