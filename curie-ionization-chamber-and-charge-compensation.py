"""Functional Curie measurement schematic and chosen charge-balance model."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np


def ground(ax, x, y):
    ax.plot([x, x], [y + 0.35, y], color='#444444', lw=1.4)
    for offset, width in [(0, 0.45), (-0.12, 0.30), (-0.24, 0.15)]:
        ax.plot([x - width, x + width], [y + offset, y + offset], color='#444444', lw=1.3)


def main():
    plt.rcParams.update({'font.size': 10, 'axes.titlesize': 12})
    fig, (ax, chart) = plt.subplots(1, 2, figsize=(12.8, 5.8), dpi=120,
                                  gridspec_kw={'width_ratios': [1.2, 1]})
    fig.patch.set_facecolor('white')
    ax.set(xlim=(0, 12), ylim=(0, 9.8), title='Ionization current balanced by calibrated charge')
    ax.axis('off')
    ax.add_patch(Rectangle((0.8, 3.4), 4.5, 0.20, color='#5a7184'))
    ax.add_patch(Rectangle((0.8, 6.25), 4.5, 0.20, color='#5a7184'))
    ax.add_patch(Rectangle((1.05, 3.60), 3.9, 0.17, color='#b36c3c'))
    ax.text(2.95, 2.98, 'B: powdered sample on biased plate', ha='center', fontsize=9)
    ax.text(2.95, 6.73, 'A: charge-sensing plate', ha='center', fontsize=10)
    ax.text(2.95, 5.03, 'Air ionized by radiation', ha='center', fontsize=10)
    for x in [1.5, 2.9, 4.3]:
        ax.annotate('', xy=(x, 6.16), xytext=(x, 5.37),
                    arrowprops={'arrowstyle': '->', 'color': '#ac3e3e', 'lw': 1.5})
        ax.text(x - 0.15, 5.42, '+', color='#ac3e3e', fontsize=12)
        ax.annotate('', xy=(x, 3.85), xytext=(x, 4.56),
                    arrowprops={'arrowstyle': '->', 'color': '#245c87', 'lw': 1.5})
        ax.text(x - 0.40, 4.40, '−', color='#245c87', fontsize=12)
    ax.plot([0.8, 0.35, 0.35], [3.5, 3.5, 2.1], color='#444444', lw=1.4)
    ax.text(0.35, 1.65, '+V', ha='center', fontweight='bold')
    ax.text(5.0, 0.55, 'Chosen polarity; battery return is grounded', ha='center', fontsize=8.5)
    ax.plot([5.3, 7.4, 10.2], [6.35, 6.35, 6.35], color='#444444', lw=1.4)
    ax.plot([7.4, 7.4], [6.35, 4.60], color='#444444', lw=1.4)
    ax.add_patch(Circle((7.4, 4.0), 0.60, edgecolor='#444444', facecolor='white', lw=1.5))
    ax.text(7.4, 4.0, 'E', ha='center', va='center', fontsize=13)
    ax.text(7.4, 1.90, 'Electrometer:\nobserve zero imbalance', ha='center', va='top', fontsize=9)
    ax.plot([7.4, 7.4], [3.4, 2.8], color='#444444', lw=1.4)
    ground(ax, 7.4, 2.45)
    ax.plot([10.2, 10.2], [6.35, 4.8], color='#444444', lw=1.4)
    ax.add_patch(Rectangle((9.82, 3.1), 0.76, 1.7, edgecolor='#444444', facecolor='#dce8ed', lw=1.4))
    ax.text(10.2, 3.95, 'Q', ha='center', va='center', fontsize=13)
    ax.text(11.0, 4.6, 'Quartz', ha='left', fontsize=9)
    ax.text(10.2, 2.5, 'Known gradual load\n→ calibrated charge', ha='center', va='top', fontsize=9)
    ax.annotate('', xy=(10.2, 1.25), xytext=(10.2, 2.10),
                arrowprops={'arrowstyle': '->', 'color': '#444444', 'lw': 1.4})
    ax.plot([10.58, 11.4, 11.4], [3.95, 3.95, 2.0], color='#444444', lw=1.2)
    ground(ax, 11.4, 1.65)
    # An optional grounding contact resets the sensing electrode before measurement.
    ax.plot([5.8, 5.8], [6.35, 7.65], color='#444444', lw=1.2)
    ax.plot([5.8, 6.45], [7.65, 8.0], color='#444444', lw=1.2)
    ax.plot([6.65, 7.1], [7.65, 7.65], color='#444444', lw=1.2)
    ground(ax, 7.1, 7.30)
    ax.text(6.35, 8.35, 'Grounding contact open during measurement', ha='center', fontsize=8.5)
    time = np.linspace(0, 30, 121)
    signal = 10 * time
    chart.plot(time, signal, color='#ac3e3e', lw=2.0, label='Collected charge: +It')
    chart.plot(time, -signal, color='#245c87', lw=2.0, label='Quartz compensation: −It')
    chart.plot(time, 0 * time, color='#2c7b44', lw=2.5, label='Sensing-node net charge: 0')
    chart.set(xlabel='Elapsed time (seconds)', ylabel='Charge (picocoulombs)',
              xlim=(0, 30), ylim=(-345, 345), title='Chosen constant-current balance: I = 10 pA')
    chart.annotate('+300 pC', xy=(30, 300), xytext=(21, 245), fontsize=10)
    chart.annotate('−300 pC', xy=(30, -300), xytext=(21, -265), fontsize=10)
    chart.grid(alpha=0.18)
    chart.legend(loc='upper left', fontsize=8.5, framealpha=0.95)
    fig.text(0.5, 0.025, 'Functional reconstruction, not a replica drawing. Model charge traces are not historical measured data.',
             ha='center', fontsize=9)
    fig.tight_layout(rect=(0, 0.065, 1, 1), w_pad=2)
    fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
