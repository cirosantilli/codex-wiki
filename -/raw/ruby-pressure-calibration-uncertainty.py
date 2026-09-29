"""Plot an original synthetic shift calibration and its uncertainty budget.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; the output is written into the current directory.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    shifts = np.array([1., 2., 3.])
    reference = np.array([2.69, 5.42, 8.09])
    slope = shifts @ reference / (shifts @ shifts)
    delta = 2.0
    ua, ul, u0, k_t, ut = 0.020, 0.010, 0.010, 0.010, 0.50
    components = np.array([delta*ua, slope*ul, slope*u0, slope*k_t*ut])
    total = np.linalg.norm(components)
    fig, (cal, err) = plt.subplots(1, 2, figsize=(11.5, 6.0), facecolor='white',
                                  gridspec_kw={'width_ratios': [1.05, 1]})
    fig.subplots_adjust(left=0.075, right=0.965, bottom=0.26, top=0.77, wspace=0.56)
    fig.suptitle('A synthetic ruby-pressure calibration and uncertainty budget', fontsize=17, y=0.97)
    fig.text(0.5, 0.89, 'All points, sensitivities and uncertainties are stipulated; no historical measurements are plotted.',
             ha='center', fontsize=10)
    xx = np.linspace(0, 3.3, 200)
    cal.plot(xx, slope*xx, color='#246c9a', lw=2, label='Fit through reference zero')
    cal.scatter(shifts, reference, color='#152c3e', s=48, zorder=4, label='Synthetic reference points')
    cal.plot([delta, delta], [0, slope*delta], color='#b72e55', ls=':')
    cal.plot([0, delta], [slope*delta, slope*delta], color='#b72e55', ls=':')
    cal.scatter([delta], [slope*delta], facecolors='white', edgecolors='#b72e55', s=120, linewidths=2, zorder=5)
    cal.annotate('Chosen reading\n2.00 nm → 5.40 GPa', xy=(delta, slope*delta),
                 xytext=(0.25, 7.65), fontsize=11,
                 arrowprops={'arrowstyle': '->', 'color': '#b72e55'}, color='#b72e55')
    cal.text(0.18, 0.62, 'a = 2.70 GPa/nm', fontsize=12, color='#246c9a')
    cal.set(xlim=(0, 3.35), ylim=(0, 9.3), xlabel='Corrected line shift D (nm)', ylabel='Pressure relative to reference (GPa)')
    cal.legend(loc='upper left', bbox_to_anchor=(-0.015, -0.16), frameon=False, fontsize=9)
    cal.set_title('Response fit', loc='left', fontsize=13, pad=12)
    labels = ['Slope calibration', 'Loaded line position', 'Reference line position', 'Temperature correction', 'Combined standard uncertainty']
    values = np.r_[components, total]
    colors = ['#246c9a', '#4d8b40', '#88ad6c', '#d09b34', '#b72e55']
    bars = err.barh(np.arange(5), values, color=colors, height=0.58)
    err.invert_yaxis()
    err.set(yticks=np.arange(5), yticklabels=labels, xlim=(0, .071), xlabel='Standard contribution (GPa)')
    err.set_xticks([0, .02, .04, .06])
    err.tick_params(axis='y', labelsize=9)
    for b, v in zip(bars, values):
        err.text(v+.0014, b.get_y()+b.get_height()/2, f'{v:.4f}', va='center', fontsize=10)
    err.set_title('Independent contributions', loc='left', fontsize=13, pad=12)
    fig.text(0.75, 0.12, r'$u_p=\sqrt{0.0400^2+0.0270^2+0.0270^2+0.0135^2}$', ha='center', fontsize=11)
    fig.text(0.75, 0.065, 'Standard uncertainty ≠ a specified confidence interval', ha='center', fontsize=10)
    fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), dpi=100, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
