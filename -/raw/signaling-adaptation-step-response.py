"""Original feedforward toy curves; write basename.png to CWD.

Tested with Python 3.14.4, numpy 2.3.5 and matplotlib 3.10.7 (Debian build).
Time is in seconds. Activities are normalized and dimensionless, not data.
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.titlesize': 12})
    t = np.linspace(-1, 25, 2601)
    elapsed = np.maximum(t, 0)
    s = (t >= 0).astype(float)
    x = -np.expm1(-elapsed)
    a = -np.expm1(-elapsed / 5)
    r = np.exp(-elapsed / 5) - np.exp(-elapsed)
    peak_t = 5 * np.log(5) / 4
    peak_r = 4 * 5 ** (-0.25) / 5

    fig, axes = plt.subplots(2, 1, figsize=(9.0, 6.3), dpi=120,
                             sharex=True, facecolor='white')
    ax = axes[0]
    ax.step(t, s, where='post', color='#263746', ls='--', lw=2,
            label='Input s: held at 1')
    ax.plot(t, x, color='#18769a', lw=2.3, label='Fast x: time constant 1 s')
    ax.plot(t, a, color='#b54838', lw=2.3, label='Slow a: time constant 5 s')
    ax.set(title='Input stays on; both branches approach 1', ylim=(-0.07, 1.16),
           ylabel='Normalized activity\n(dimensionless)')
    ax.legend(loc='lower right', framealpha=1, facecolor='white', fontsize=10)
    ax = axes[1]
    ax.plot(t, r, color='#7752a5', lw=2.7, label=r'Readout $r=x-a=e^{-t/5}-e^{-t}$ for $t\geq0$')
    ax.axhline(0, color='#606870', ls=':', lw=1)
    ax.scatter([peak_t], [peak_r], color='#7752a5', zorder=4)
    ax.annotate(f'Peak: {peak_t:.4f} s\nr = {peak_r:.5f}',
                xy=(peak_t, peak_r), xytext=(5.8, 0.43), fontsize=11,
                arrowprops={'arrowstyle': '->', 'color': '#7752a5'})
    ax.annotate('Approaches baseline 0\ndespite sustained input', xy=(21, np.exp(-21 / 5) - np.exp(-21)),
                xytext=(12.5, 0.20), fontsize=11,
                arrowprops={'arrowstyle': '->', 'color': '#7752a5'})
    ax.set(title='A pulse from fast activation and slower opposition',
           xlabel='Time (seconds)', ylabel='Normalized readout r\n(dimensionless)',
           xlim=(-1, 25), ylim=(-0.04, 0.66))
    ax.legend(loc='upper right', framealpha=1, facecolor='white', fontsize=10)
    for ax in axes:
        ax.axvline(0, color='#9ba5ad', ls=':', lw=1)
        ax.spines[['top', 'right']].set_visible(False)
        ax.grid(color='#e3e9ed', lw=0.7)
        ax.set_axisbelow(True)
    fig.suptitle('Adaptation without feedback: a simple feedforward toy', fontsize=15, y=0.98)
    fig.text(0.5, 0.02, 'Chosen values, not measurements. The readout feeds back to neither branch.',
             ha='center', fontsize=10, color='#4c5861')
    fig.subplots_adjust(left=0.12, right=0.98, bottom=0.13, top=0.88, hspace=0.28)
    path = Path.cwd() / Path(__file__).with_suffix('.png').name
    fig.savefig(path, facecolor='white', transparent=False)
    plt.close(fig)
    print(f'Wrote {path.name}: 1080 × 756 pixels')


if __name__ == '__main__':
    main()
