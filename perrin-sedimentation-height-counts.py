"""Original optical-layer geometry and chosen equilibrium profile.

Tested with Python 3.14, matplotlib 3.10.7 and numpy 2.3.5.
Run from _media; output is perrin-sedimentation-height-counts.png in CWD.
All numerical inputs and expected counts are illustrative, not Perrin's data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
import numpy as np


def main():
    k_b, temperature, radius, contrast, gravity = 1.380649e-23, 298.0, 0.250e-6, 200.0, 9.81
    volume = 4 * np.pi * radius**3 / 3
    scale_um = k_b * temperature / (contrast * volume * gravity) * 1e6
    levels = np.array([0.0, 20.0, 40.0, 60.0])
    counts = 400 * np.exp(-levels / scale_um)
    colors = ['#007c91', '#dd7223', '#6956b3', '#a83d66']
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False, 'axes.spines.right': False})
    fig = plt.figure(figsize=(12.0, 5.4), facecolor='white')
    grid = fig.add_gridspec(1, 3, width_ratios=[1.45, 1, 1], left=.035, right=.98,
                           top=.78, bottom=.18, wspace=.38)
    geometry, profile, logarithm = [fig.add_subplot(grid[0, j]) for j in range(3)]
    fig.suptitle('Counting a miniature atmosphere', fontsize=18, y=.97)
    fig.text(.5, .88, 'Chosen model: a = 0.250 μm, density contrast = 200 kg/m³, T = 298 K; H = %.2f μm' % scale_um,
             ha='center', fontsize=11)

    geometry.set(xlim=(-.18, 1.70), ylim=(-22, 134))
    geometry.axis('off')
    geometry.add_patch(Rectangle((0, -5), 1, 100, facecolor='#eef5fb', edgecolor='#3e5d78', linewidth=1.6))
    geometry.add_patch(Rectangle((0, -9), 1, 4, facecolor='#9eb9ce', edgecolor='none'))
    geometry.add_patch(Rectangle((0, 95), 1, 3, facecolor='#9eb9ce', edgecolor='none'))
    geometry.add_patch(Polygon([[.30, 131], [.70, 131], [.59, 113], [.41, 113]],
                              closed=True, facecolor='#536170'))
    geometry.annotate('', xy=(.5, 99), xytext=(.5, 113),
                      arrowprops={'arrowstyle': '->', 'color': '#283747', 'lw': 1.7})
    geometry.text(1.06, 122, 'Objective\nviews down', va='center')
    geometry.text(1.06, 98, 'Cover glass', va='center')
    geometry.text(1.06, -7, 'Slide / floor', va='center')
    geometry.annotate('', xy=(-.08, 95), xytext=(-.08, -5),
                      arrowprops={'arrowstyle': '<->', 'color': '#536170'})
    geometry.text(-.13, 45, '100 μm chamber', rotation=90, va='center', ha='right', fontsize=10)
    geometry.add_patch(Rectangle((0, 19), 1, 2, color=colors[1], alpha=.27))
    # A fixed schematic population is generated from the same truncated exponential.
    rng = np.random.default_rng(1742)
    h = -scale_um * np.log(1 - rng.random(90) * (1 - np.exp(-100 / scale_um))) - 5
    x = rng.uniform(.035, .965, len(h))
    geometry.scatter(x, h, s=12, c='#365a76', alpha=.65, edgecolors='none')
    for level, color in zip(levels, colors):
        geometry.plot([0, 1], [level, level], color=color, lw=1.4, ls='--')
        geometry.text(1.06, level, f'z = {level:g} μm', color=color, va='center', fontsize=10)
    geometry.annotate('Focused slab\nδ = 2 μm', xy=(.25, 20), xytext=(.4, 73),
                      ha='center', arrowprops={'arrowstyle': '->', 'color': colors[1]},
                      color=colors[1], fontsize=10,
                      bbox={'facecolor': 'white', 'edgecolor': 'none', 'alpha': .9})
    geometry.text(.5, -20, 'Reference z = 0 is 5 μm above floor\nOther dashed layers: refocus and recount',
                  ha='center', va='top', fontsize=9.5)
    geometry.set_title('Equal optical volumes', fontsize=12, pad=13)

    z = np.linspace(0, 80, 300)
    profile.plot(400 * np.exp(-z / scale_um), z, color='#34495e', lw=2)
    profile.scatter(counts, levels, c=colors, s=45, zorder=3)
    for count, level, color in zip(counts, levels, colors):
        profile.annotate(f'{count:.1f}', (count, level), xytext=(6, 7),
                         textcoords='offset points', color=color, fontsize=10)
    profile.set(xlabel='Expected count, equal effort', ylabel='Height z (μm)', xlim=(0, 470), ylim=(-3, 83))
    profile.set_title('Exponential profile', fontsize=12, pad=13)
    profile.grid(alpha=.2)

    logarithm.plot(z, -z / scale_um, color='#34495e', lw=2)
    logarithm.scatter(levels, np.log(counts / 400), c=colors, s=45, zorder=3)
    logarithm.set(xlabel='Height z (μm)', ylabel='ln [mean count(z) / mean count(0)]', xlim=(-3, 83), ylim=(-2.7, .15))
    logarithm.text(6, -2.45, 'Slope = −1/H\n= −%.5f μm⁻¹' % (1 / scale_um), fontsize=10)
    logarithm.set_title('Same counts, logarithmic scale', fontsize=11.5, pad=13)
    logarithm.grid(alpha=.2)
    fig.text(.65, .035, 'Original schematic and exact model expectations; not historical measurements.\nGeometry is functional, with particle sizes and slab thickness exaggerated.',
             ha='center', fontsize=10, color='#47535e')
    output = Path.cwd() / f'{Path(__file__).stem}.png'
    fig.savefig(output, dpi=110, facecolor='white')
    plt.close(fig)
    print(output)


if __name__ == '__main__':
    main()
