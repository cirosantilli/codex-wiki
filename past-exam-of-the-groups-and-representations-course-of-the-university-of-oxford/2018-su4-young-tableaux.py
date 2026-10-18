"""Construct the exterior-power tableaux, not copied exam art. Python 3.14."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.size': 14, 'figure.facecolor': 'white'})
fig, axes = plt.subplots(1, 4, figsize=(10, 4.8), layout='constrained')
labels = [r'$\mathbf{1}=\Lambda^0 U$', r'$\mathbf{4}=U$', r'$\mathbf{6}=\Lambda^2 U$', r'$\overline{\mathbf{4}}=\Lambda^3 U$']
tensors = [r'$S$', r'$v^i$', r'$T^{[ij]}$', r'$T^{[ijk]}\ \leftrightarrow\ w_\ell$']
weights = ['(0, 0, 0)', '(1, 0, 0)', '(0, 1, 0)', '(0, 0, 1)']
for count, ax in enumerate(axes):
    ax.set_xlim(-0.7, 0.7)
    ax.set_ylim(-0.8, 3.9)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(labels[count], fontsize=17, pad=16)
    if count == 0:
        ax.text(0, 2.05, 'empty', ha='center', va='center', fontsize=14, color='#666666')
    for j in range(count):
        y = 3.1-(j+1)*0.72
        ax.add_patch(Rectangle((-0.36, y), 0.72, 0.72, facecolor='white', edgecolor='#205c96', linewidth=2))
        ax.text(0, y+0.36, str(j+1), ha='center', va='center', fontsize=17)
    ax.text(0, 0.15, tensors[count], ha='center', va='center', fontsize=16)
    ax.text(0, -0.45, weights[count], ha='center', va='center', fontsize=12)
fig.suptitle(r'$SU(4)$: one-column tableaux give antisymmetric tensors', fontsize=17)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
