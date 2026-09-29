"""Generate an original Yukawa fermion-box schematic in the caller's cwd."""
import os
os.environ.setdefault('MPLBACKEND', 'Agg')
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7.2, 3.5), dpi=100)
fig.patch.set_facecolor('white')
ax.set_facecolor('white')
v = [(-1, -.65), (1, -.65), (1, .65), (-1, .65)]
for i, (x, y) in enumerate(v):
    xx, yy = v[(i + 1) % 4]
    ax.plot([x, xx], [y, yy], color='#183b50', lw=2)
    ax.annotate('', xy=(.35*x+.65*xx, .35*y+.65*yy),
                xytext=(.65*x+.35*xx, .65*y+.35*yy),
                arrowprops=dict(arrowstyle='-|>', lw=1.8, color='#183b50'))
    ex, ey = 1.7*x, 1.7*y
    ax.plot([x, ex], [y, ey], '--', color='#ad5e13', lw=1.8)
    ax.text(ex, ey+.14*(1 if y>0 else -1), rf'$\phi(p_{i+1})$',
            ha='center', va='center', fontsize=13)
    ax.scatter([x], [y], s=25, color='#183b50', zorder=4)
ax.text(0, 0, 'Closed fermion loop', ha='center', fontsize=12)
ax.text(0, -1.50, 'Solid arrows: spinor propagators   •   Dashed lines: scalar legs',
        ha='center', fontsize=10)
ax.set_xlim(-2.45, 2.45)
ax.set_ylim(-1.72, 1.60)
ax.set_title('Yukawa four-scalar fermion box', fontsize=14, pad=8)
ax.axis('off')
fig.subplots_adjust(left=.03, right=.97, bottom=.02, top=.87)
fig.savefig('paper-44-yukawa-box.png', dpi=100, facecolor='white')
plt.close(fig)
