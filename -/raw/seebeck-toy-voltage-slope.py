"""Generate calculated toy Seebeck calibration lines, never measured data.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../seebeck-toy-voltage-slope.py
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    delta_t = np.linspace(-50, 50, 401)
    s_a, s_b = 25., -15.  # Stipulated microvolts per kelvin, constant.
    voltage_mv = (s_a - s_b) * delta_t / 1000
    fig, ax = plt.subplots(figsize=(7.6, 4.9), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.axhline(0, color='#a5a5a5', lw=1)
    ax.axvline(0, color='#a5a5a5', lw=1)
    ax.plot(delta_t, voltage_mv, color='#176b83', lw=3, label='A minus B: positive input on A')
    ax.plot(delta_t, -voltage_mv, color='#b85c22', lw=2.5, ls='--', label='Reversed inputs: B minus A')
    ax.scatter([0, 50], [0, 2], color='#176b83', s=45, zorder=5, clip_on=False)
    ax.annotate('50 K → +2.00 mV', (50, 2), xytext=(4, 1.55), arrowprops={'arrowstyle': '->', 'color': '#176b83'}, color='#176b83')
    ax.annotate('Same junction temperatures\nzero in the ideal model', (0, 0), xytext=(-46, .45), fontsize=11, bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2}, arrowprops={'arrowstyle': '->', 'color': '#555555'})
    ax.text(4, -1.75, 'Slope: $S_A-S_B$\n= 40 µV/K', color='#176b83', fontsize=12)
    ax.set(xlim=(-53, 53), ylim=(-2.45, 2.75), xlabel=r'$\Delta T=T_h-T_c$ (K), with $T_c=20$ °C fixed', ylabel='Meter reading (mV)')
    ax.set_xticks([-50, -25, 0, 25, 50])
    ax.set_yticks([-2, -1, 0, 1, 2])
    ax.grid(alpha=.16)
    ax.spines[['top', 'right']].set_visible(False)
    ax.legend(loc='upper left', fontsize=10, frameon=True, facecolor='white', framealpha=1)
    fig.suptitle('Toy linear calibration — calculated, not measured', fontsize=15, weight='bold', y=.98)
    fig.text(.5, .025, 'Stipulated constant coefficients: $S_A=25$ µV/K, $S_B=-15$ µV/K', ha='center', fontsize=11)
    fig.subplots_adjust(left=.12, right=.97, bottom=.18, top=.88)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
