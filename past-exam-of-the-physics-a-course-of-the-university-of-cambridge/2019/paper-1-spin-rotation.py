"""Original spin preparation/rotation/analyser diagram; Python 3.14, NumPy 2.3, Matplotlib 3.10."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

fig, (apparatus, ax) = plt.subplots(2, 1, figsize=(9, 5.8), gridspec_kw={'height_ratios': [1, 1.5]}, layout='constrained')
fig.set_facecolor('white')
apparatus.set(xlim=(-.2, 10.2), ylim=(-1.4, 1.4))
apparatus.axis('off')
for x, width, label, color in [(1, 1.7, 'Prepare +z\nSG + aperture', '#dbeafe'), (4, 2, 'Uniform field Bx\nTransit time ℓ/v', '#e0f2df'), (7.3, 1.5, 'Analyse Sz\nSecond SG', '#dbeafe')]:
    apparatus.add_patch(FancyBboxPatch((x, -.55), width, 1.1, boxstyle='round,pad=0.08', facecolor=color, edgecolor='#334155'))
    apparatus.text(x + width/2, 0, label, ha='center', va='center', fontsize=10)
for start, end in [((0, 0), (.9, 0)), ((2.8, 0), (3.9, 0)), ((6.1, 0), (7.2, 0)), ((8.9, 0), (9.65, .8)), ((8.9, 0), (9.65, -.8))]:
    apparatus.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle': '->', 'lw': 1.7})
apparatus.text(9.75, .8, '+z', va='center')
apparatus.text(9.75, -.8, '−z', va='center')
apparatus.text(.2, -.9, 'collimated\nbeam', ha='center', fontsize=9)
apparatus.set_title('Spatial separation reads out a spin rotated by a uniform field', fontsize=12)
theta = np.linspace(0, 4*np.pi, 600)
ax.plot(theta/np.pi, np.cos(theta/2)**2, lw=2.2, label=r'$P(+z)=\cos^2(\theta/2)$')
ax.plot(theta/np.pi, np.sin(theta/2)**2, lw=2.2, ls='--', label=r'$P(-z)=\sin^2(\theta/2)$')
ax.set(xlabel=r'Rotation angle $\theta/\pi$, with $\theta=\lambda B\ell/v$', ylabel='Fraction of transmitted beam', xlim=(0, 4), ylim=(-.03, 1.12))
ax.legend(loc='upper center', ncol=2, fontsize=10)
ax.grid(alpha=.2)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
