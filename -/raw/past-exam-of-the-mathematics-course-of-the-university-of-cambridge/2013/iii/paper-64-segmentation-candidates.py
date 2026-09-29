"""Original synthetic segmentation candidates; output to caller cwd.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
The two-region mask is stipulated, not computed as a global minimizer.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

N = 192
RADIUS = 0.27
BETA = 0.025
rng = np.random.default_rng(201364)
x = (np.arange(N) + 0.5) / N
xx, yy = np.meshgrid(x, x)
inside = (xx - 0.5) ** 2 + (yy - 0.5) ** 2 < RADIUS ** 2
truth = np.where(inside, 0.8, 0.2)
observed = np.clip(truth + rng.normal(0, 0.08, (N, N)), 0, 1)
one_region = np.full_like(observed, observed.mean())
two_regions = np.where(inside, observed[inside].mean(), observed[~inside].mean())
fidelity_one = np.mean((one_region - observed) ** 2)
fidelity_two = np.mean((two_regions - observed) ** 2)
edge_cost = BETA * 2 * np.pi * RADIUS
fig, axes = plt.subplots(1, 3, figsize=((1120 + 1e-6)/100, (380 + 1e-6)/100), dpi=100)
fig.patch.set_facecolor('white')
fig.suptitle('Two candidate geometries: fitting contrast versus paying for an interface', fontsize=13, y=0.98)
items = [(observed, 'Observed synthetic data', 'Original noise realization'),
         (one_region, 'One-region least-squares mean', f'Fidelity = {fidelity_one:.3f}; edge cost = 0'),
         (two_regions, 'Two-region least-squares means', f'Fidelity = {fidelity_two:.3f}; edge cost = {edge_cost:.3f}')]
for ax, (values, title, footer) in zip(axes, items):
    ax.imshow(values, origin='lower', extent=(0, 1, 0, 1), cmap='gray', vmin=0, vmax=1)
    ax.set_title(title, fontsize=11)
    ax.set_xlabel(footer, fontsize=10)
    ax.set_xticks([])
    ax.set_yticks([])
axes[2].add_patch(plt.Circle((0.5, 0.5), RADIUS, fill=False, color='#d95f02', linewidth=1.5))
fig.subplots_adjust(left=0.025, right=0.975, bottom=0.13, top=0.82, wspace=0.12)
fig.savefig(Path.cwd()/'paper-64-segmentation-candidates.png', dpi=100, facecolor='white', transparent=False)
plt.close(fig)
