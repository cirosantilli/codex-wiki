"""Original evidence map, not a measured tree or reconstruction of sequence data.

Python 3.14, matplotlib 3.10.7. Run from _media to save the matching PNG.
The lower panel abstracts the logic of Stegemann and Bock (2006), not their
physical construct map. Protein import was not demonstrated by that experiment.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

BLUE = '#1b5976'
GREEN = '#26734d'
PURPLE = '#75518d'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12})
fig, ax = plt.subplots(figsize=(12.8, 8.2), dpi=100)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 12.8), ylim=(0, 8.2))
ax.axis('off')


def text(x, y, value, size=12, **kwargs):
    ax.text(x, y, value, ha='center', va='center', fontsize=size, **kwargs)


def box(x, y, w, h, title, detail, color=BLUE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.10',
                              facecolor='white', edgecolor=color, linewidth=1.8))
    text(x + w / 2, y + h - 0.29, title, 13, weight='bold', color=color)
    text(x + w / 2, y + (h - 0.35) / 2 - 0.03, detail, 11)


def arrow(start, end, color=BLUE):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle='-|>', color=color,
                                mutation_scale=15, linewidth=1.6))


text(6.4, 7.84, 'Different evidence answers different questions', 20,
     weight='bold', color=BLUE)
box(0.45, 5.48, 3.65, 1.58, 'Ancestry',
    'Comparable sequences + alignment\n→ inferred evolutionary affinity\nCheck sampling and model sensitivity.')
box(4.55, 5.48, 3.65, 1.58, 'DNA relocation',
    'Organelle DNA in nuclear genome\n→ transfer / integration\nPresence alone does not imply function.', PURPLE)
box(8.65, 5.48, 3.65, 1.58, 'Functional activation',
    'Expression + inherited phenotype\n→ activity in the new setting\nDestination of protein is another test.', GREEN)
text(6.4, 7.31, 'These are distinct inferences, not three measurements on one scale.', 12,
     color='#555555')
text(6.4, 4.94, 'Tobacco experiment: separate transfer from activation', 16,
     weight='bold', color=BLUE)
box(0.65, 3.45, 4.80, 1.08, 'Transfer selected',
    'Engineered plastid segment enters nucleus;\nselection uses nuclear nptII expression.', PURPLE)
box(7.35, 3.45, 4.80, 1.08, 'Silent transferred aadA',
    'Engineered plastids replaced by ordinary plastids;\nplants initially sensitive to both test drugs.', PURPLE)
arrow((5.65, 4.00), (7.15, 4.00), PURPLE)
arrow((9.75, 3.31), (9.75, 2.97), GREEN)
box(7.35, 1.63, 4.80, 1.20, 'Selected nuclear activation',
    'Dual-drug-resistant regenerated plants;\nMendelian inheritance + aadA RNA;\nsequence mapping connects gene to promoter.', GREEN)
box(0.65, 1.63, 4.80, 1.20, 'Alternative explanations checked',
    'Both drugs: reduce single-drug mutants.\nReciprocal crosses: plastid vs nuclear inheritance.\nOriginal-line / ordinary-plant DNA controls.', BLUE)
arrow((5.65, 2.22), (7.15, 2.22), BLUE)
ax.add_patch(FancyBboxPatch((0.65, 0.45), 11.50, 0.65,
                          boxstyle='round,pad=0.08', facecolor='#fafafa',
                          edgecolor='#d1d1d1', linewidth=1))
text(6.4, 0.78, 'Separate requirement: delivery of a nuclear-encoded protein back into the organelle.', 12,
     weight='bold', color=BLUE)
text(6.4, 0.15, 'Original schematic. No measured tree, sequence map, response magnitude or historical timeline is shown.', 11,
     color='#555555')
fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
fig.savefig(Path.cwd() / f'{Path(__file__).stem}.png', facecolor='white')
plt.close(fig)
