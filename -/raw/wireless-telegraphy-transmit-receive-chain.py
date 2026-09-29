"""Functional historical radio chain; Python 3.14, matplotlib 3.10.7.

Run from _media: MPLBACKEND=Agg python ../wireless-telegraphy-transmit-receive-chain.py
The drawing is an original explanatory abstraction, not a wiring diagram.
"""
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(11, 7), dpi=120, facecolor='white')
ax.set(xlim=(0, 11), ylim=(0, 7)); ax.axis('off')
blue, orange, green = '#176b99', '#b75c15', '#28754b'

def box(x, y, w, h, text, color=blue):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                               facecolor='#f7fafc', edgecolor=color, linewidth=1.6))
    ax.text(x+w/2, y+h/2, text, ha='center', va='center', color='#172832')

def arrow(a, b, color=blue, dashed=False):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle='-|>', mutation_scale=14,
                                linewidth=1.6, color=color,
                                linestyle='--' if dashed else '-'))

ax.text(.3, 6.7, 'Wireless telegraphy: excite → radiate → select → detect → record',
        fontsize=16, weight='bold')
ax.text(.3, 6.26, 'Functional synthesis of early coherer reception and later tuned coupling', fontsize=11)
box(.35, 4.65, 2.0, 1.0, 'Power supply\n+ telegraph key')
box(3.0, 4.65, 2.4, 1.0, 'Spark gap + C₁ + L₁\nclosed oscillating loop')
arrow((2.45, 5.15), (2.88, 5.15))
box(6.1, 4.65, 2.25, 1.0, 'L₂ + elevated wire\ntransmitting antenna')
arrow((5.52, 5.15), (5.98, 5.15)); ax.text(5.74, 5.88, 'inductive\ncoupling', ha='center', color=blue)
ax.plot([7.22, 7.22], [4.56, 4.18], color=blue)
for yy, ww in [(4.18,.54),(4.07,.36),(3.96,.18)]:
    ax.plot([7.22-ww/2, 7.22+ww/2], [yy,yy], color=blue, lw=1.7)
ax.text(8.48, 4.22, 'earth return', color=blue)
arrow((8.48, 5.15), (10.15, 3.6), orange, True)
ax.text(9.63, 5.08, 'propagating\nradio wave', ha='center', color=orange)
box(8.35, 2.05, 2.25, 1.0, 'Receiving antenna\n+ earth + L₃')
box(4.75, 2.05, 2.8, 1.0, 'L₄ + tuning capacitor\n+ coherer detector')
arrow((8.23, 2.55), (7.68, 2.55)); ax.text(7.92, 3.23, 'inductive\ncoupling', ha='center', color=blue)
box(.35, 2.05, 3.45, 1.0, 'Local cell → relay → recorder\nreceiver power is local', green)
arrow((4.63, 2.55), (3.93, 2.55), green)
box(4.75, .55, 2.8, .65, 'Tapper resets coherer', green)
arrow((2.3, 1.94), (4.63, .88), green)
arrow((6.15, 1.32), (6.15, 1.94), green)
ax.text(.35, .63, 'Key held: many damped trains\nKey released: no intended trains', color=orange)
ax.text(8.1, .63, 'Tuning precedes detection.\nA trace is not an RF waveform.', color='#394b55')
fig.subplots_adjust(left=.015, right=.985, top=.99, bottom=.02)
fig.savefig(Path(__file__).stem+'.png', facecolor='white')
