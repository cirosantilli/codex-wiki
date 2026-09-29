"""Original conceptual schematic; Python 3.14, matplotlib 3.10.7.

Run from _media; output goes to the working directory, with this script's stem.
No sizes, rates, historical dates or ancestral host morphology are inferred.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch, FancyBboxPatch

BLUE = '#1b5976'
GREEN = '#26734d'
PURPLE = '#75518d'
ORANGE = '#a45b1d'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(12.8, 7.2), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 12.8), ylim=(0, 7.2))
ax.axis('off')


def text(x, y, value, size=12, **kwargs):
    return ax.text(x, y, value, ha='center', va='center', fontsize=size, **kwargs)


def arrow(start, end, color=BLUE, style='-|>', **kwargs):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle=style,
                                mutation_scale=16, linewidth=1.8,
                                color=color, **kwargs))


def cell(x, integrated=False):
    ax.add_patch(Ellipse((x, 4.30), 3.1, 2.25, facecolor='#f0f7fb',
                        edgecolor=BLUE, linewidth=2))
    # Generic internal partner: shape is neither a phylogeny nor a micrograph.
    ax.add_patch(Ellipse((x + 0.48, 4.28), 1.08, 0.66,
                        facecolor='#e0f0e6', edgecolor=GREEN, linewidth=2))
    ax.add_patch(Ellipse((x + 0.48, 4.28), 0.30, 0.24,
                        facecolor='none', edgecolor=GREEN, linewidth=1.4))
    text(x + 0.48, 3.65, 'organelle' if integrated else 'partner', 11,
         color=GREEN)
    if integrated:
        ax.add_patch(Ellipse((x - 0.85, 4.45), 0.65, 0.75,
                            facecolor='#f1e9f7', edgecolor=PURPLE, linewidth=1.8))
        text(x - 0.85, 4.45, 'nuclear\nDNA', 9, color=PURPLE)
        arrow((x + 0.13, 4.56), (x - 0.50, 4.63), PURPLE)
        text(x - 0.15, 5.12, 'DNA transfer', 10, color=PURPLE)
        arrow((x - 0.52, 4.20), (x + 0.06, 4.15), ORANGE)
        text(x - 0.10, 3.36, 'protein delivery', 10, color=ORANGE)
    else:
        text(x - 0.58, 4.55, 'host', 12, color=BLUE)


text(6.4, 6.72, 'Endosymbiosis: location is the beginning of the question', 20,
     weight='bold', color=BLUE)
text(6.4, 6.23, 'Conceptual integration — not a dated sequence or a mandatory order', 12,
     color='#555555')
for x, title, detail, integrated in [
    (2.1, 'Internal association', 'One organism inside another;\nbenefit and permanence are separate questions.', False),
    (6.4, 'Inherited partnership', 'Persistence and exchange;\ncoordination with host division.', False),
    (10.7, 'Integrated organelle', 'Nuclear genes can supply proteins;\nloss of independent capabilities.', True),
]:
    text(x, 5.72, title, 15, weight='bold', color=BLUE)
    cell(x, integrated)
    text(x, 2.76, detail, 11)
arrow((3.80, 4.30), (4.68, 4.30))
arrow((8.10, 4.30), (8.98, 4.30))
ax.add_patch(FancyBboxPatch((0.65, 0.63), 11.5, 1.38,
                          boxstyle='round,pad=0.15', facecolor='#fafafa',
                          edgecolor='#d1d1d1', linewidth=1))
text(6.4, 1.70, 'Bacterial ancestry of two familiar organelle lineages', 13,
     weight='bold')
text(3.55, 1.20, 'Alphaproteobacterial ancestry → mitochondria', 12, color=BLUE)
text(9.00, 1.20, 'Cyanobacterial ancestry → plant plastids', 12, color=GREEN)
text(6.4, 0.20, 'Modern relatives are not literal ancestor species. Host outline and partner shape are generic.', 11,
     color='#555555')
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.savefig(Path.cwd() / f'{Path(__file__).stem}.png', facecolor='white')
plt.close(fig)
