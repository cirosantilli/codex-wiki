"""Generate an idealized thermocouple schematic; values are toy, not data.

Run from _media: MPLCONFIGDIR=/tmp/codex-wiki-matplotlib python ../seebeck-thermocouple-experiment.py
Tested with Python 3.14.4, Matplotlib 3.10.7, NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch


def main():
    plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=120)
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    ax.set(xlim=(0, 10), ylim=(0, 5.3))
    ax.axis('off')
    ax.text(5, 5.05, 'Thermocouple: read A relative to B', ha='center', weight='bold', fontsize=17)
    cold = FancyBboxPatch((2.4, 1.2), 1.75, 2.6, boxstyle='round,pad=0.12', facecolor='#eaf4fc', edgecolor='#3678a8')
    hot = FancyBboxPatch((7.45, 1.6), 1.9, 1.75, boxstyle='round,pad=0.12', facecolor='#fff1e5', edgecolor='#c75a13')
    ax.add_patch(cold)
    ax.add_patch(hot)
    ax.plot([3.25, 7.1, 8.3], [3.2, 3.2, 2.5], color='#ad5219', lw=4)
    ax.plot([3.25, 7.1, 8.3], [1.8, 1.8, 2.5], color='#28758e', lw=4)
    ax.text(5.5, 3.45, 'Material A', color='#ad5219', ha='center', weight='bold')
    ax.text(5.5, 1.4, 'Material B (reference)', color='#28758e', ha='center', weight='bold')
    for y in (3.2, 1.8):
        ax.plot([3.25, 1.05, 1.05], [y, y, 2.5 + (0.45 if y > 2.5 else -0.45)], color='#555555', lw=2)
        ax.plot(3.25, y, 'o', color='#303030', ms=6)
    ax.plot(8.3, 2.5, 'o', color='#303030', ms=8)
    ax.add_patch(Circle((1.05, 2.5), .45, facecolor='white', edgecolor='#303030', lw=2))
    ax.text(1.05, 2.5, 'V', ha='center', va='center', fontsize=17)
    ax.text(1.3, 2.99, '+', fontsize=17, weight='bold')
    ax.text(1.3, 1.94, '−', fontsize=17, weight='bold')
    ax.text(1.05, 1.35, 'High input resistance\n$ I \\approx 0 $', ha='center', va='top', fontsize=11)
    ax.text(3.25, 4.12, 'Two reference connections\nat the same $T_c$', ha='center', va='bottom')
    ax.text(3.25, 2.5, '$T_c = 20$ °C\n(toy)', ha='center', va='center', fontsize=11)
    ax.text(8.3, 3.67, 'A–B measuring junction', ha='center', va='bottom')
    ax.text(8.3, 2.0, '$T_h = 70$ °C\n(toy)', ha='center', va='top', fontsize=11)
    ax.text(1.1, 3.83, 'Identical\nmeter leads', ha='center', fontsize=11, color='#555555')
    ax.text(5, .68, r'$V_{AB}=V_A-V_B=\int_{T_c}^{T_h}(S_A-S_B)\,dT$', ha='center', fontsize=16)
    ax.text(5, .16, 'Toy: $S_A-S_B=40$ µV/K,  $\\Delta T=50$ K  →  reading +2.00 mV', ha='center', fontsize=12)
    fig.subplots_adjust(left=.025, right=.985, bottom=.025, top=.99)
    fig.savefig(Path(__file__).stem + '.png', facecolor='white', transparent=False)
    plt.close(fig)


if __name__ == '__main__':
    main()
