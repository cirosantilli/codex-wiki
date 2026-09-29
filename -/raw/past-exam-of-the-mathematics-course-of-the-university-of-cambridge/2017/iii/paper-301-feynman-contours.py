"""Original QFT energy-contour schematic. Python 3.14; matplotlib 3.10.7, numpy 2.3.5.
Run from the desired output directory; writes a same-basename opaque PNG there.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), dpi=100, facecolor='white')
for ax, sign, color in zip(axes, [-1, 1], ['#1764ab', '#b64c14']):
    ax.set_facecolor('white')
    radius = 2.35
    ax.axhline(0, color='#444444', lw=1)
    ax.axvline(0, color='#aaaaaa', lw=0.8)
    ax.annotate('', xy=(radius, 0), xytext=(-radius, 0), arrowprops=dict(arrowstyle='->', color=color, lw=2))
    theta = np.linspace(0, sign*np.pi, 200)
    ax.plot(radius*np.cos(theta), radius*np.sin(theta), '--', color=color, lw=1.8)
    t0, t1 = sign*0.46*np.pi, sign*0.52*np.pi
    ax.annotate('', xy=(radius*np.cos(t1),radius*np.sin(t1)), xytext=(radius*np.cos(t0),radius*np.sin(t0)), arrowprops=dict(arrowstyle='->', color=color, lw=2))
    for energy, imag, text in [(1.05, -0.22, r'$+E-i0$'), (-1.05, 0.22, r'$-E+i0$')]:
        selected = imag*sign > 0
        ax.scatter([energy], [imag], color='#b00020' if selected else '#666666', s=45, zorder=4)
        ax.text(energy, imag + (0.18 if imag>0 else -0.38), text, ha='center', fontsize=11)
    ax.text(2.36, 0.18, r'$\mathrm{Re}\,p^0$', ha='right', fontsize=10)
    ax.text(0.1, 2.42, r'$\mathrm{Im}\,p^0$', fontsize=10)
    ax.set_title(r'$\tau>0$: close below, clockwise' if sign<0 else r'$\tau<0$: close above, counterclockwise', fontsize=12, pad=11)
    ax.text(0, sign*1.18, 'Selected pole shown in red', ha='center', color=color, fontsize=10)
    ax.set(xlim=(-2.7, 2.7), ylim=(-2.6, 2.7), aspect='equal')
    ax.set_xticks([]); ax.set_yticks([])
    for spine in ax.spines.values(): spine.set_visible(False)
fig.subplots_adjust(left=0.025, right=0.975, bottom=0.055, top=0.88, wspace=0.04)
output = Path.cwd() / (Path(__file__).stem + '.png')
fig.savefig(output, dpi=100, facecolor='white', transparent=False)
plt.close(fig)
print(output)
print('matplotlib', matplotlib.__version__, 'numpy', np.__version__)
