"""Draw an original escape/readout model. Python 3.14; NumPy 2.3.5; Matplotlib 3.10.7.

Run from _media; writes this script's basename.png to the current directory.
All plotted curves are stipulated constant-hazard calculations, not measurements.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch


def main():
    plt.rcParams.update({'font.size': 12, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(10.5, 6.5), dpi=100, facecolor='white')
    flow = fig.add_axes([.03, .61, .94, .25]); flow.axis('off'); flow.set_xlim(-.025, 1.025)
    labels = [r'Reset trapped phase' + '\n' + r'Ramp current: $dI/dt=r$',
              'Escape from phase well\nMay retrap: no event yet',
              'Sustained phase advance\nVoltage event → record $I_{sw}$']
    for x, label in zip([.01, .35, .69], labels):
        box = FancyBboxPatch((x, .30), .29, .60, boxstyle='round,pad=0.012',
                             ec='#3b5d79', fc='#f1f6fa', lw=1.5)
        flow.add_patch(box)
        flow.text(x + .145, .60, label, ha='center', va='center', fontsize=11,
                  linespacing=1.6)
    for start, end in [(.302, .345), (.642, .685)]:
        flow.annotate('', (end, .60), (start, .60),
                      arrowprops={'arrowstyle': '->', 'lw': 1.8, 'color': '#3b5d79'})
    flow.text(.5, .06, 'Repeat preparation → distribution of switching currents → escape rate',
              ha='center', va='center', color='#3b5d79', fontsize=12)
    left = fig.add_axes([.09, .16, .36, .34])
    right = fig.add_axes([.60, .16, .36, .34])
    t_ms = np.linspace(0, 4, 501)
    left.plot(t_ms, np.exp(-t_ms), color='#1565a8', lw=2.5)
    median = np.log(2)
    left.plot([0, median, median], [.5, .5, 0], '--', color='#a3631f', lw=1.4)
    left.text(1.2, .63, 'Half remain at\n0.693147 ms', fontsize=11, color='#94561a')
    left.set(xlim=(0, 4), ylim=(0, 1.04), xlabel='Elapsed time (ms)',
             ylabel='Trapped fraction S(t)', title='Survival at fixed escape rate')
    di_na = np.linspace(0, 4, 501)
    right.plot(di_na, np.exp(-di_na), color='#267f73', lw=2.5)
    right.fill_between(di_na[di_na <= median], np.exp(-di_na[di_na <= median]),
                       color='#267f73', alpha=.20)
    right.axvline(1, color='#a3631f', ls='--', lw=1.4)
    right.text(1.3, .68, 'Mean increment\n1 nA', color='#94561a', fontsize=11)
    right.text(.12, .13, 'Area ≈ 1/2', fontsize=10, color='#267f73')
    right.set(xlim=(0, 4), ylim=(0, 1.04), xlabel=r'Current increment $I-I_0$ (nA)',
              ylabel=r'Density p(I) (per nA)', title='Current distribution under a ramp')
    for ax in [left, right]:
        ax.grid(alpha=.18)
    fig.suptitle('Escape becomes a voltage event; statistics recover a rate', y=.96, fontsize=16)
    fig.text(.5, .555, 'Chosen model: Γ = 1000 s⁻¹, r = 1 μA/s • perfect detection • no retrapping',
             ha='center', fontsize=11, color='#555555')
    fig.text(.5, .045, r'$p(I)=\Gamma(I)S(I)/r$     •     synthetic curves, not historical data',
             ha='center', fontsize=12, color='#444444')
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
