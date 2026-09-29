"""Original product-connectivity explanation; Python 3.14/numpy/matplotlib.

The macrocycle has 14 atoms: ten carbons and four oxygens. No E/Z assignment.
Output is a PNG basename in the current working directory.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from tools.chemistry_diagram import bond, atom, finish

fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.7), layout='constrained')
fig.patch.set_facecolor('white')
# Ring sequence C=C-C-O-C-C-O-C-C-O-C-C-O-C, then close to initial C.
labels = ['CH', 'CH', 'CH$_2$', 'O', 'CH$_2$', 'CH$_2$', 'O',
          'CH$_2$', 'CH$_2$', 'O', 'CH$_2$', 'CH$_2$', 'O', 'CH$_2$']
angle = np.linspace(np.pi/2+.22, np.pi/2+.22-2*np.pi, 14, endpoint=False)
pts = np.column_stack([2.15*np.cos(angle), 2.15*np.sin(angle)])
ax = axes[0]
for i in range(14):
    if i == 0:
        a, b = pts[i], pts[i+1]
        offset = np.array([0.0, .055])
        for sign in [-1, 1]:
            aa, bb = a+sign*offset, b-sign*offset
            ax.plot([aa[0], bb[0]], [aa[1], bb[1]], color='.2', lw=1.6)
    else:
        bond(ax, pts[i], pts[(i+1)%14])
for pos, label in zip(pts, labels):
    atom(ax, pos, label, size=10.8, color='#b65c38' if label == 'O' else '.15')
ax.text(0, .05, 'Z: cyclic polyether\n14 ring atoms\n4 oxygen donors\nE/Z unspecified', ha='center',
        va='center', fontsize=12, color='#286a85')
finish(ax, (-2.65, 2.65), (-2.7, 2.8), 'Intramolecular ring closure')
ax = axes[1]
ax.text(.5, .84, 'Y: intermolecular metathesis polymer', transform=ax.transAxes,
        ha='center', fontsize=12, color='#286a85')
ax.text(.5, .60, r'$[\! -\!\mathrm{CH{=}CH{-}CH_2{-}O{-}(CH_2CH_2{-}O)_3{-}CH_2}\!-\!]_n$',
        transform=ax.transAxes, ha='center', fontsize=13)
ax.text(.5, .40, 'Same internal connectivity per repeat;\nopen chains instead of one closed ring.',
        transform=ax.transAxes, ha='center', fontsize=11)
ax.text(.5, .17, r'Volatile coproduct U: $\mathrm{CH_2{=}CH_2}$',
        transform=ax.transAxes, ha='center', fontsize=12)
ax.text(.5, .06, 'Terminal groups depend on conversion and work-up.',
        transform=ax.transAxes, ha='center', fontsize=9, color='.4')
ax.axis('off')
fig.savefig('paper-1-metathesis-products.png', dpi=150, facecolor='white')
plt.close(fig)
