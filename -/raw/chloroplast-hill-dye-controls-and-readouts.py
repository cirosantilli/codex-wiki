"""Original Hill-assay comparison and readout logic; no measured data.
Python 3.14; matplotlib 3.10.7. Writes basename.png to CWD.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

INK = '#203342'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 12, 'text.color': INK})
fig, ax = plt.subplots(figsize=(12, 8.4), dpi=110)
fig.patch.set_facecolor('white')
ax.set(xlim=(0, 12), ylim=(0, 8.4)); ax.axis('off')

def box(x, y, w, h, fc, text='', size=12):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0,rounding_size=0.10', fc=fc, ec='#8b9da8', lw=1.1))
    if text:
        ax.text(x+w/2, y+h/2, text, ha='center', va='center', fontsize=size)

def arrow(start, end):
    ax.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle': '->', 'lw': 1.6, 'color': INK})

ax.text(.3, 8.02, 'Hill assays: match the inference to the readout', fontsize=20, weight='bold')
ax.text(.3, 7.61, 'Original logic schematic • conditional comparisons • no experimental data', fontsize=11)
box(.3, 6.6, 2.9, .69, '#eef5e8', 'Cold leaf preparation')
arrow((3.25, 6.94), (3.65, 6.94))
box(3.7, 6.6, 3.6, .69, '#eef5e8', 'Grind → filter → centrifuge')
arrow((7.35, 6.94), (7.75, 6.94))
box(7.8, 6.6, 3.9, .69, '#eef5e8', 'Resuspend collected fraction')
ax.text(.3, 6.23, 'Modern DCPIP assay: compare matched mixtures', fontsize=14, weight='bold')
# No colors here represent actual experimental outcomes.
headers=['Mixture / condition', 'Question tested']
ax.text(.52, 5.76, headers[0], weight='bold')
ax.text(6.22, 5.76, headers[1], weight='bold')
rows=[('Extract + dye, light', 'Test condition'),
      ('Extract + dye, dark', 'Does removing light remove the effect?'),
      ('Dye, light; no extract', 'Does dye change without the preparation?'),
      ('Extract, light; no dye', 'What color comes from the extract?'),
      ('Supernatant + dye', 'Did active material remain in the liquid?')]
for i, (left, right) in enumerate(rows):
    y=5.06-i*.48
    box(.3,y,11.4,.43,'#f2f6f8' if i%2==0 else '#ffffff')
    ax.text(.52,y+.215,left,va='center',fontsize=12)
    ax.text(6.22,y+.215,right,va='center',fontsize=12)
ax.text(.3, 2.80, 'Three questions require distinct evidence', fontsize=14, weight='bold')
box(.3, 1.16, 3.55, 1.32, '#e7f0fb', 'DYE REDUCTION\nLoss of blue DCPIP\nElectron-transfer readout', 12)
box(4.22, 1.16, 3.55, 1.32, '#eaf4f1', 'OXYGEN EVOLUTION\nSeparate oxygen readout\nHill 1937: hemoglobin\noxygenation spectrum', 11.5)
box(8.15, 1.16, 3.55, 1.32, '#fff4dc', 'CARBON FIXATION\nEvidence of CO₂ carbon\nentering organic material', 12)
ax.text(6, .73, 'A dye endpoint alone supplies neither an oxygen amount nor a carbon-fixation rate.', ha='center', fontsize=12, weight='bold')
ax.text(6, .33, 'Modern assay and historical oxygen indicator are separate methods, not one combined apparatus.', ha='center', fontsize=10.5)
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', dpi=110)
plt.close(fig)
