"""Generate the channel profile in caller CWD; tested with Python 3.14.4.

Uses root numpy/matplotlib dependencies and honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

b = 30.0
xi = np.linspace(-1.0, 1.0, 2001)
coth_b = 1.0 / np.tanh(b)
profile = (2.0 * np.exp(b * (xi - 1.0)) / (1.0 - np.exp(-2.0 * b))
           - coth_b - xi + 1.5 * (coth_b - 1.0 / b) * (1.0 - xi**2))
fig, ax = plt.subplots(figsize=(10, 5), dpi=120, facecolor='white')
ax.set_facecolor('white')
ax.axhline(0.0, color='#737373', linewidth=0.9)
ax.axvline(-1.0, color='#303030', linewidth=2)
ax.axvline(1.0, color='#303030', linewidth=2)
ax.fill_between(xi, 0, profile, where=profile >= 0, color='#d9eaf4')
ax.fill_between(xi, 0, profile, where=profile <= 0, color='#f6dfce')
ax.plot(xi, profile, color='#144c71', linewidth=2.4)
ax.annotate('Upward return flow', xy=(-0.45, 0.55), xytext=(-0.81, 1.04),
            arrowprops={'arrowstyle': '->', 'color': '#144c71'}, fontsize=11)
ax.annotate('Downward cell-driven flow', xy=(0.72, -1.1), xytext=(-0.05, -1.55),
            arrowprops={'arrowstyle': '->', 'color': '#98552c'}, fontsize=11)
ax.annotate('Illuminated wall', xy=(1.0, 0.0), xytext=(0.48, 0.70),
            arrowprops={'arrowstyle': '->', 'color': '#303030'}, fontsize=11)
ax.set(xlim=(-1.08, 1.08), ylim=(-1.85, 1.24), xlabel=r'Cross-channel position $x/a$',
       ylabel=r'Vertical velocity $w/W$ (positive upwards)',
       title=r'Phototactic channel flow: $\beta a=30$, $W=g^{\prime}n_0a^2/(\mu\beta a)$')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(axis='x', color='#e6e6e6', linewidth=0.6)
fig.tight_layout()
fig.savefig('paper-77-channel-profile.png', facecolor='white', transparent=False)
plt.close(fig)
