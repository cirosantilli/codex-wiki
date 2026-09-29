"""Four modular roots and their greatest-common-divisor factor extraction.

Output goes to CWD; environment/dependencies are specified in pyproject.toml.
"""
from pathlib import Path
from math import gcd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

modulus, residue, reference = 77, 15, 13
roots = [z for z in range(modulus) if z*z % modulus == residue]
assert roots == [13, 20, 57, 64]
fig, ax = plt.subplots(figsize=(9.6, 5.0), dpi=120, facecolor='white')
ax.set_facecolor('white'); ax.set_xlim(-0.7, 2.05); ax.set_ylim(-0.45, 2.7); ax.axis('off')
row_residues = [6, 1]; column_residues = [2, 9]
for row, mod7 in enumerate(row_residues):
    for col, mod11 in enumerate(column_residues):
        candidates = [z for z in roots if z%7 == mod7 and z%11 == mod11]
        assert len(candidates) == 1
        z = candidates[0]; y = 1-row
        useful = z in [20, 57]
        fill = '#dceee3' if useful else '#e6ebf1'
        ax.add_patch(Rectangle((col, y), 1, 1, facecolor=fill, edgecolor='#687784', linewidth=1.2))
        minus, plus = gcd(z-reference, modulus), gcd(z+reference, modulus)
        ax.text(col+0.5, y+0.66, f'z = {z}', ha='center', va='center', fontsize=20, fontweight='bold', color='#176c91' if z == reference else '#274a38' if useful else '#4c5b67')
        ax.text(col+0.5, y+0.31, f'gcd(z − 13, 77) = {minus}\ngcd(z + 13, 77) = {plus}', ha='center', va='center', fontsize=10)
for col, label in enumerate(['z ≡ +2 mod 11', 'z ≡ −2 mod 11']): ax.text(col+0.5, 2.12, label, ha='center', fontsize=12)
for row, label in enumerate(['z ≡ −1\nmod 7', 'z ≡ +1\nmod 7']): ax.text(-0.12, 1.5-row, label, ha='right', va='center', fontsize=12)
ax.text(0.75, 2.5, 'Four roots of z² ≡ 15 (mod 77)', ha='center', fontsize=17)
ax.text(0.75, -0.22, 'Green: mixed signs give proper factors 7 and 11.\nGray: same or opposite signs give only 1 and 77.', ha='center', fontsize=11)
fig.subplots_adjust(left=0.035, right=0.98, top=0.98, bottom=0.035)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'), facecolor='white')
plt.close(fig)
