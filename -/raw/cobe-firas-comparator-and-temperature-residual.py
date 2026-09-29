"""Functional FIRAS comparison and an original Planck temperature-shift model.

Run from _media; tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
The curves are calculations, never COBE data. Output is opaque white PNG.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

BASENAME = Path(__file__).stem
H, K, C = 6.62607015e-34, 1.380649e-23, 299792458.0
T0, DT = 2.725, 0.001


def planck(nu, temperature):
    return 2 * H * nu**3 / C**2 / np.expm1(H * nu / (K * temperature))


def main():
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    fig = plt.figure(figsize=(11, 7.2), layout='constrained')
    grid = fig.add_gridspec(2, 2, height_ratios=[0.9, 1.25])
    ax = fig.add_subplot(grid[0, :])
    ax.set(xlim=(0, 11), ylim=(0, 3.3)); ax.axis('off')
    ax.set_title('FIRAS: compare against a reference, then calibrate the comparison', loc='left', pad=12)

    def box(x, y, w, h, label, color):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05',
                                   fc=color, ec='#425466', lw=1.4))
        ax.text(x+w/2, y+h/2, label, ha='center', va='center')

    box(.15, 1.95, 2.25, .8, 'Sky entrance', '#e7f0fd')
    box(.15, .35, 2.25, .8, 'Internal blackbody\nadjustable temperature', '#fff0d8')
    box(3.5, 1.05, 2.5, 1.1, 'Differential\ninterferometer', '#edf3f5')
    box(7.0, 1.05, 3.5, 1.1, 'Cold bolometers\n→ spectral difference', '#e7f3e9')
    for start, end in [((2.45, 2.35), (3.45, 1.9)), ((2.45, .75), (3.45, 1.3)),
                       ((6.05, 1.6), (6.95, 1.6))]:
        ax.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle': '->', 'lw': 1.6})
    ax.text(1.275, 3.0, 'External calibrator covers entrance', ha='center', fontsize=10)
    ax.annotate('', xy=(1.275, 2.77), xytext=(1.275, 2.9), arrowprops={'arrowstyle': '->'})
    ax.text(5.6, .22, 'Functional diagram; not an optical layout', ha='center', color='#526273', fontsize=10)

    nu = np.linspace(10, 650, 1100) * 1e9
    b0, b1 = planck(nu, T0), planck(nu, T0+DT)
    peak = b0.max()
    x = H * nu / (K * T0)
    linear = b0 / T0 * x / (-np.expm1(-x)) * DT
    a = fig.add_subplot(grid[1, 0])
    a.plot(nu/1e9, b0/peak, color='#2166ac', lw=2, label='2.725 K')
    a.plot(nu/1e9, b1/peak, color='#cb521d', lw=1.5, ls='--', label='2.726 K')
    a.set(xlabel='Frequency ν (GHz)', ylabel='Radiance / fixed reference peak',
          title='Chosen blackbodies almost overlap', xlim=(0, 650), ylim=(0, 1.08))
    a.legend(frameon=False); a.grid(alpha=.2)
    a = fig.add_subplot(grid[1, 1])
    a.plot(nu/1e9, (b1-b0)/peak*1e6, color='#cb521d', lw=2, label='Exact difference')
    a.plot(nu/1e9, linear/peak*1e6, color='#2166ac', lw=1.5, ls='--', label='Temperature derivative')
    a.set(xlabel='Frequency ν (GHz)', ylabel='Difference / fixed peak (parts per million)',
          title='A temperature mismatch leaves a residual', xlim=(0, 650))
    a.legend(frameon=False); a.grid(alpha=.2)
    fig.suptitle('Calculated spectra with ΔT = 1 mK — no measured data', fontsize=14)
    fig.savefig(BASENAME+'.png', dpi=100, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
