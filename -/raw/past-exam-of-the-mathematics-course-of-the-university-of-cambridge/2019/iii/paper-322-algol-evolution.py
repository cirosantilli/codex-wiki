#!/usr/bin/env python3
"""Draw a qualitative HR diagram for an Algol pair, writing a PNG to cwd."""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(9, 5.2), dpi=100, facecolor='white')
ax.set_facecolor('white')
# Dimensionless plotting coordinates: qualitative ordering only, not a stellar model.
main_sequence = np.array([[0.10, 0.91], [0.28, 0.70], [0.39, 0.56], [0.58, 0.31], [0.81, 0.08]])
donor = np.array([[0.39, 0.56], [0.47, 0.65], [0.61, 0.76], [0.75, 0.75], [0.79, 0.55]])
accretor = np.array([[0.58, 0.31], [0.50, 0.42], [0.39, 0.56], [0.28, 0.70]])
stripped = np.array([[0.79, 0.55], [0.65, 0.54], [0.41, 0.55], [0.16, 0.57]])
cooling = np.array([[0.16, 0.57], [0.12, 0.34], [0.18, 0.14], [0.30, 0.08]])
ax.plot(*main_sequence.T, color='#bcbcbc', lw=9, alpha=0.45, label='Main sequence (schematic)')
ax.plot(*donor.T, color='#ac4e32', lw=2.4, label='Donor: initially more massive')
ax.plot(*accretor.T, color='#226a96', lw=2.4, label='Accretor: initially less massive')
ax.plot(*stripped.T, color='#ac4e32', ls='--', lw=1.8, label='Later donor stripping and cooling')
ax.plot(*cooling.T, color='#ac4e32', ls='--', lw=1.8)
for track, color in [(donor, '#ac4e32'), (accretor, '#226a96'), (stripped, '#ac4e32'), (cooling, '#ac4e32')]:
    for i in [1]:
        start = track[i]
        end = start + 0.55 * (track[i+1] - start)
        ax.annotate('', xy=end, xytext=start,
                    arrowprops={'arrowstyle': '->', 'color': color, 'lw': 2})
ax.scatter(*donor[0], color='#ac4e32', s=45, zorder=4)
ax.scatter(*accretor[0], color='#226a96', s=45, zorder=4)
ax.scatter(*donor[-1], color='#ac4e32', marker='*', s=130, zorder=4)
ax.scatter(*accretor[-1], color='#226a96', marker='*', s=130, zorder=4)
ax.annotate('Initial donor', xy=donor[0], xytext=(0.44, 0.58), fontsize=10,
            arrowprops={'arrowstyle': '-', 'color': '#777'})
ax.annotate('Initial accretor', xy=accretor[0], xytext=(0.64, 0.20), fontsize=10,
            arrowprops={'arrowstyle': '-', 'color': '#777'})
ax.annotate('Cool evolved donor\n(later less massive)', xy=donor[-1], xytext=(0.66, 0.36), fontsize=10,
            arrowprops={'arrowstyle': '->', 'color': '#ac4e32'})
ax.annotate('Hot mass gainer', xy=accretor[-1], xytext=(0.17, 0.83), fontsize=10,
            arrowprops={'arrowstyle': '->', 'color': '#226a96'})
ax.text(0.57, 0.84, 'Expansion toward the giant branch', fontsize=10)
ax.annotate('Envelope stripped', xy=(0.38, 0.55), xytext=(0.33, 0.43), fontsize=10,
            arrowprops={'arrowstyle': '->', 'color': '#ac4e32'})
ax.text(0.04, 0.02, 'Low-mass core:\nhelium white dwarf', fontsize=10)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('Effective temperature (hotter left, cooler right)', fontsize=11)
ax.set_ylabel('Luminosity (increases upward)', fontsize=11)
ax.set_title('An Algol pair on a qualitative Hertzsprung–Russell diagram', fontsize=13)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=2, fontsize=9, frameon=False)
fig.subplots_adjust(left=0.10, right=0.97, bottom=0.22, top=0.91)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white')
plt.close(fig)
