"""Original matched-assay workflow and hypothetical stoichiometric calculation.

No measured absorbance data are plotted. The model assumes complete reduction,
matched accessibility, one TNB per thiol, no reductant, and identical final protein
concentrations. Run from _media. Python 3.14 / Matplotlib 3.10.7 / NumPy 2.3.5.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

INK, BLUE, AMBER = '#23313e', '#27689c', '#a96108'
EPSILON, PATH_CM, PROTEIN_M = 14150., 1., 10e-6
FREE_THIOLS, BRIDGES = 2, 2
BEFORE_M = PROTEIN_M * FREE_THIOLS
AFTER_M = PROTEIN_M * (FREE_THIOLS + 2 * BRIDGES)
A0, A1 = EPSILON * PATH_CM * BEFORE_M, EPSILON * PATH_CM * AFTER_M
assert abs((A1 - A0) / (2 * EPSILON * PATH_CM * PROTEIN_M) - BRIDGES) < 1e-12
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11})
fig, ax = plt.subplots(figsize=(10.5, 7.2), dpi=120, facecolor='white')
ax.set(xlim=(0, 10.5), ylim=(0, 7.2))
ax.axis('off')
ax.text(5.25, 6.94, 'Ellman assay: compare thiols before and after reduction',
        ha='center', va='center', size=16, weight='bold', color=INK)
ax.text(5.25, 6.57, 'Match accessibility, recovery and dilution before interpreting the difference.',
        ha='center', color=INK)


def box(x, y, w, h, label, face='#f3f7fb', edge=BLUE):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.04',
                              facecolor=face, edgecolor=edge, lw=1.5))
    ax.text(x+w/2, y+h/2, label, ha='center', va='center', color=INK,
            linespacing=1.35)


def arrow(a, b):
    ax.annotate('', xy=b, xytext=a,
                arrowprops={'arrowstyle': '->', 'lw': 1.6, 'color': BLUE})


box(.2, 4.4, 1.45, .85, 'Purified protein\nsplit aliquots')
arrow((1.65, 4.82), (2.05, 5.62))
arrow((1.65, 4.82), (2.05, 4.07))
box(2.1, 5.05, 2.7, 1.1, 'BEFORE\nNo reduction\nMatched cleanup')
box(2.1, 3.45, 2.7, 1.2, 'AFTER\nComplete reduction\nRemove reducing reagent', face='#fff8e9', edge=AMBER)
arrow((4.85, 5.6), (5.3, 5.6))
arrow((4.85, 4.05), (5.3, 4.05))
box(5.35, 5.05, 2.35, 1.1, 'Fresh excess DTNB\nDetect free thiols')
box(5.35, 3.5, 2.35, 1.1, 'Fresh excess DTNB\nDetect all exposed thiols')
arrow((7.75, 5.6), (8.18, 5.6))
arrow((7.75, 4.05), (8.18, 4.05))
box(8.23, 5.05, 2.0, 1.1, f'20 µM thiols\nA₄₁₂ = {A0:.3f}', face='#fff9cf', edge=AMBER)
box(8.23, 3.5, 2.0, 1.1, f'60 µM thiols\nA₄₁₂ = {A1:.3f}', face='#ffe888', edge=AMBER)
ax.text(5.25, 3.08, 'MODEL VALUES ONLY: 10 µM protein, 2 free thiols + 2 bridges per molecule',
        ha='center', weight='bold', color=AMBER, size=11)

ax.add_patch(Rectangle((.35, .8), 9.8, 1.88, facecolor='#f7f8fa', edgecolor='#ccd4dc'))
ax.text(.6, 2.42, 'Read yellow TNB at 412 nm', weight='bold', color=INK)
box(.6, 1.25, 1.1, .65, '412 nm\nlight', face='white')
ax.add_patch(Rectangle((2.2, 1.03), .7, 1.12, facecolor='#fff0a4', edgecolor=INK, lw=1.5))
arrow((1.76, 1.57), (2.17, 1.57))
arrow((2.94, 1.57), (3.35, 1.57))
box(3.4, 1.25, 1.2, .65, 'Detector', face='white')
ax.text(2.55, .88, '1 cm path', ha='center', size=10, color=INK)
ax.text(5.0, 2.06, f'ΔA = {A1:.3f} − {A0:.3f} = {A1-A0:.3f}', color=INK, size=13)
ax.text(5.0, 1.56, 'Bridge concentration = ΔA / (2 ε l) = 20 µM', color=INK, size=12)
ax.text(5.0, 1.06, '20 µM bridges / 10 µM protein = 2 bridges per molecule', color=INK, size=11)
ax.text(5.25, .49, 'Controls: DTNB blank • cysteine standards • processed blank • matched sample background',
        ha='center', size=10, color=INK)
ax.text(5.25, .17, 'Original workflow and analytical model • ε = 14,150 L mol⁻¹ cm⁻¹ • no measured data',
        ha='center', size=10, color='#56616d')
fig.subplots_adjust(left=.01, right=.99, top=.99, bottom=.02)
fig.savefig(Path(__file__).with_suffix('.png').name, facecolor='white', transparent=False)
plt.close(fig)
