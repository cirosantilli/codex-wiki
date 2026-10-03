"""Draw the cyclic jump graphs; tested with Python 3.14, NumPy and Matplotlib.
Run from the desired output directory; writes paper-4-fleas.png there.
"""
import numpy as np
import matplotlib.pyplot as plt

points = np.array([[0, 1], [-0.86, -0.5], [0.86, -0.5]])
fig, axes = plt.subplots(1, 2, figsize=(7.2, 3.3), facecolor='white')
for ax, direction, rate, title in zip(axes, [1, -1], ['1', r'$\rho$'], ['First flea', 'Second flea']):
    for i, p in enumerate(points):
        q = points[(i + direction) % 3]
        delta = q - p
        start, end = p + 0.14 * delta, q - 0.14 * delta
        ax.annotate('', xy=end, xytext=start, arrowprops=dict(arrowstyle='->', lw=2, color='#245d8c'))
        middle = (p + q) / 2
        middle += 0.15 * middle / np.linalg.norm(middle)
        ax.text(*middle, rate, ha='center', va='center', fontsize=13)
        ax.scatter(*p, s=390, facecolor='white', edgecolor='#245d8c', zorder=3)
        ax.text(*p, 'ABC'[i], ha='center', va='center', fontsize=12, zorder=4)
    ax.set_title(title, fontsize=13)
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-0.95, 1.35)
    ax.set_aspect('equal')
    ax.axis('off')
fig.tight_layout()
fig.savefig('paper-4-fleas.png', dpi=160, facecolor='white')
plt.close(fig)
