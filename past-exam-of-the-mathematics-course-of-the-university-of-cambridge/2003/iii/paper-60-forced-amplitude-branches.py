"""Original forced-amplitude diagrams; Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.

Run from the desired output directory. The sole image output is a CWD basename.
MPLCONFIGDIR is controlled by the caller and is never changed here.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D

OUTPUT = Path('paper-60-forced-amplitude-branches.png')
COLORS = ['#126b8a', '#df981d', '#bb3d51']


def positive_real_roots(coefficients):
    roots = np.roots(coefficients)
    return sorted(r.real for r in roots if abs(r.imag) < 1e-7 and r.real > 0)


def main():
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 4.0), dpi=125, sharey=True)
    for ax, detuning, heading in zip(axes, [0.95, 0.83, 0.70], ['(a) No folds', '(b) Two folds and Hopf', '(c) Two folds, no Hopf']):
        intensity = np.linspace(0.002, 1.0 / detuning**2, 12001)
        for branch_sign in [-1, 1]:
            parameter = intensity + branch_sign * np.sqrt(np.maximum(1.0 / intensity - detuning**2, 0.0))
            radius = np.sqrt(intensity)
            points = np.column_stack([parameter, radius])
            midpoint_s = (intensity[1:] + intensity[:-1]) / 2
            midpoint_mu = (parameter[1:] + parameter[:-1]) / 2
            trace = 2 * (midpoint_mu - 2 * midpoint_s)
            determinant = (midpoint_mu - 3 * midpoint_s) * (midpoint_mu - midpoint_s) + detuning**2
            status = np.where(determinant < 0, 1, np.where(trace < 0, 0, 2))
            segments = np.stack([points[:-1], points[1:]], axis=1)
            ax.add_collection(LineCollection(segments, colors=[COLORS[i] for i in status], linewidths=2.5))
        if detuning < np.sqrt(3) / 2:
            folds = positive_real_roots([4 * detuning**2, -4, 0, 0, 1])
            for s in folds:
                mu = s + 1 / (2 * s**2)
                ax.plot(mu, np.sqrt(s), 'o', color='black', markersize=4.0)
                offset = (-30, -20) if s < 1 else (10, 6)
                ax.annotate('fold', (mu, np.sqrt(s)), xytext=offset, textcoords='offset points', fontsize=8)
        if detuning > 2**(-1 / 3):
            s = positive_real_roots([1, 0, detuning**2, -1])[0]
            ax.plot(2 * s, np.sqrt(s), 'D', color='#613c8e', markersize=5)
            ax.annotate('Hopf', (2 * s, np.sqrt(s)), xytext=(8, -20), textcoords='offset points', fontsize=8, color='#613c8e')
        ax.set_title(heading + '\n' + rf'$\Lambda={detuning:.2f}$', fontsize=10)
        ax.set_xlim(-1.5, 3.4)
        ax.set_ylim(0, 1.62)
        ax.set_xlabel(r'$\mu$')
        ax.grid(alpha=0.20)
        ax.spines[['top', 'right']].set_visible(False)
    axes[0].set_ylabel(r'Steady amplitude $R=|A|$')
    handles = [Line2D([0], [0], color=c, lw=2.5, label=text) for c, text in zip(COLORS, ['2 stable / 0 unstable', '1 stable / 1 unstable', '0 stable / 2 unstable'])]
    fig.legend(handles=handles, loc='lower center', ncol=3, fontsize=9, frameon=False, bbox_to_anchor=(0.5, 0.015))
    fig.suptitle('Moving forcing: steady branches and eigenvalue counts', fontsize=12)
    fig.subplots_adjust(left=0.07, right=0.985, top=0.78, bottom=0.23, wspace=0.20)
    fig.savefig(OUTPUT, facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
