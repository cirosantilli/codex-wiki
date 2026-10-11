"""Generate paper-1-q4-graph.png. Tested with Python 3.14.4,
NumPy 2.3.5 and Matplotlib 3.10.7 (repository pyproject.toml)."""
from pathlib import Path
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/nst-2025-ia-paper-1-matplotlib')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.2, 4.5), layout='constrained', facecolor='white')
for x in (np.linspace(-6, -0.15, 900), np.linspace(0.15, 6, 900)):
    ax.plot(x, x*x/4 + 4/(x*x), color='#17679a', linewidth=2)
ax.axvline(0, color='gray', linestyle='--', linewidth=1)
ax.axhline(0, color='black', linewidth=0.8)
ax.scatter([-2, 2], [2, 2], color='#b53b26', zorder=5)
for x in (-2, 2):
    ax.annotate(f'({x}, 2)', (x, 2), xytext=(0, 12), textcoords='offset points', ha='center')
ax.set(xlim=(-6, 6), ylim=(0, 12), xlabel='$x$', ylabel='$f(x)$',
       title=r'Question 4: $f(x)=x^2/4+4/x^2$')
ax.grid(alpha=0.2)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=130, facecolor='white')
plt.close(fig)
