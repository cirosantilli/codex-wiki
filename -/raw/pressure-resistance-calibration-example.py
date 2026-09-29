"""Original synthetic pressure calibration example, not historical sensor data.
Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is written to the current working directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(10, 6), dpi=110)
    ax = fig.add_axes((.10, .35, .85, .52))
    p = np.linspace(0, 1.5, 301)
    alpha, beta, delta_t = .020, .0002, 10
    ref = 1 + alpha*p
    warm = ref + beta*delta_t
    ax.plot(p, ref, color='#1675aa', lw=2.4, label='$T=T_0$, no history offset')
    ax.plot(p, warm, color='#bb5a17', lw=2.4, label='$T=T_0+10$ K, no history offset')
    for h, label in ((.0002, 'Warm histories: $h=\\pm0.0002$'), (-.0002, None)):
        ax.plot(p, warm+h, '--', lw=1.3, color='#8553a1', label=label)
    ax.hlines(1.022, 0, 1.1, color='#555', ls=':', lw=1.3)
    ax.vlines([1, 1.1], 1, 1.022, colors=['#bb5a17', '#1675aa'], linestyles=':')
    ax.scatter([1, 1.1], [1.022, 1.022], c=['#bb5a17', '#1675aa'], zorder=4)
    ax.annotate('Corrected: 1.00 GPa', (1, 1.022), (.67, 1.030),
                arrowprops={'arrowstyle': '->'}, color='#97420e')
    ax.annotate('Temperature ignored: 1.10 GPa', (1.1, 1.022), (.92, 1.009),
                arrowprops={'arrowstyle': '->'}, color='#125b86', fontsize=10)
    ax.set(xlim=(0, 1.5), ylim=(1, 1.034), xlabel='Pressure p (GPa)',
           ylabel='Resistance ratio R / R₀')
    ax.ticklabel_format(axis='y', style='plain', useOffset=False)
    ax.grid(alpha=.18)
    ax.legend(loc='upper left', framealpha=1, fontsize=10)
    fig.suptitle('A resistance reading needs temperature and history', fontsize=16, y=.97)
    fig.text(.5, .91, 'Synthetic model: R/R₀ = 1 + 0.020 p [GPa] + 0.0002 (T − T₀) [K] + h',
             ha='center', fontsize=11)
    flow = fig.add_axes((.055, .055, .90, .16))
    flow.axis('off')
    labels = ['Specimen in\npressure medium', 'Internal resistance\nsensor R(p, T, history)',
              'Electrical\nreadout R/R₀', 'Calibration + T\n→ inferred pressure']
    for i, label in enumerate(labels):
        x = .005+i*.255
        flow.add_patch(FancyBboxPatch((x, .30), .217, .55,
                                     boxstyle='round,pad=0.005',
                                     fc='#f4f7f9', ec='#607284'))
        flow.text(x+.1085, .575, label, ha='center', va='center', fontsize=10)
        if i < 3:
            flow.annotate('', (x+.250, .575), (x+.220, .575),
                          arrowprops={'arrowstyle': '->', 'color': '#607284'})
    fig.text(.5, .025, 'Illustrative coefficients and histories only; no measured manganin data.',
             ha='center', fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
