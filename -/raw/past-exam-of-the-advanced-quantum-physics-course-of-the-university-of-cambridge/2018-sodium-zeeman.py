"""Original weak-field sodium level/transition diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

fig, axes = plt.subplots(1, 2, figsize=(11, 6), layout='constrained')
colors = {-1: '#2563eb', 0: '#64748b', 1: '#d97706'}
for ax, j, g, name, center in [(axes[0], .5, 2/3, 'D1: 3p ²P₁/₂ → 3s ²S₁/₂', 7), (axes[1], 1.5, 4/3, 'D2: 3p ²P₃/₂ → 3s ²S₁/₂', 10)]:
    upper = [-.5, .5] if j == .5 else [-1.5, -.5, .5, 1.5]
    pairs = [(mu, ml) for mu in upper for ml in [-.5, .5] if abs(mu-ml) <= 1]
    for mu in upper:
        ax.hlines(center+g*mu, -.12, 5.0, color='#334155', lw=1.3)
        ax.text(5.06, center+g*mu, 'm = '+str(Fraction(mu)), va='center', fontsize=9)
    for ml in [-.5, .5]:
        ax.hlines(2*ml, -.12, 5, color='#334155', lw=1.3)
        ax.text(5.06, 2*ml, 'm = '+str(Fraction(ml)), va='center', fontsize=9)
    for index, (mu, ml) in enumerate(pairs):
        x = .25 + 4.25*index/(len(pairs)-1)
        shortest = j == 1.5 and mu == .5 and ml == -.5
        color = '#dc2626' if shortest else colors[int(mu-ml)]
        ax.annotate('', xy=(x, 2*ml+.07), xytext=(x, center+g*mu-.07), arrowprops={'arrowstyle': '-|>', 'lw': 2.6 if shortest else 1.65, 'color': color})
        shift = Fraction(g*mu-2*ml).limit_denominator(3)
        text = ('+' if shift > 0 else '')+str(shift)
        ax.text(x, 2.8 if index % 2 == 0 else 3.65, text, ha='center', va='center', fontsize=10, color=color, bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 1.5})
    ax.text(-.1, center+g*j+.55, f'Upper g = {Fraction(g).limit_denominator(3)}', fontsize=10)
    ax.text(-.1, -1.8, 'Lower g = 2', fontsize=10)
    ax.set(xlim=(-.3, 6.55), ylim=(-2.3, 14), title=name)
    ax.axis('off')
axes[0].text(0, 13.5, 'Photon shifts shown in units of μB B', fontsize=11)
axes[1].text(0, 13.5, 'Red arrow: shortest wavelength', color='#dc2626', fontsize=11)
handles = [Line2D([0],[0], color=colors[q], lw=2, label=f'mu − ml = {q:+d}') for q in [-1,0,1]]
fig.legend(handles=handles, loc='lower center', bbox_to_anchor=(.48, -.065), ncol=3, frameon=False, fontsize=10)
fig.suptitle('Allowed electronic transitions; term offsets schematic and splitting enlarged', fontsize=12)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white', bbox_inches='tight')
