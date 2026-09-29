import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1.1, 700)
fig, ax = plt.subplots(figsize=(7.2, 3.6), dpi=100, layout='constrained')
for j, offset in enumerate([-1.0, -0.45, 0.1]):
    ax.plot(x, offset+2*np.sqrt(x), color='#1765a4', linewidth=2, label='wavecrests' if j == 0 else None)
for j, offset in enumerate([0.15, 0.8, 1.45]):
    ax.plot(x, offset-2*x**1.5/3, color='#b33a32', linestyle='--', linewidth=1.7, label='rays' if j == 0 else None)
    a, b = 0.50, 0.40
    ax.annotate('', xy=(b, offset-2*b**1.5/3), xytext=(a, offset-2*a**1.5/3), arrowprops=dict(arrowstyle='->', color='#b33a32'))
ax.axvline(0, color='#333333', linewidth=2.5)
ax.text(0.035, 1.60, 'shoreline', rotation=90, va='top', fontsize=9)
ax.set(xlim=(-0.04, 1.1), ylim=(-0.55, 1.7), xlabel='Distance from shore x (scaled)', ylabel='Alongshore coordinate y (scaled)', title='Near-shore ray asymptotics for p = 1')
ax.set_aspect('equal', adjustable='box')
ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), fontsize=9)
ax.spines[['top', 'right']].set_visible(False)
fig.savefig('paper-3-shoreline-rays.png', facecolor='white', transparent=False)
plt.close(fig)
