"""Draw an original returning-geodesic construction; PNG is written in the CWD.

Tested with Python 3.14, NumPy 2.3, Matplotlib 3.10; dependencies in root pyproject.toml.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

b, a = 1.5, 4.0
radius = np.hypot(b, np.pi)
x = np.linspace(-np.pi, np.pi, 700)
y = np.sqrt(radius**2 - x*x)
fig, ax = plt.subplots(figsize=(8, 4.6), facecolor='white')
ax.fill_between([-np.pi, np.pi], b, a, color='#edf4fa')
for edge in [-np.pi, np.pi]:
    ax.plot([edge, edge], [b, a], '--', color='#607285', lw=1.3)
ax.plot([-np.pi, np.pi], [b, b], color='#607285', lw=1)
ax.plot([-np.pi, np.pi], [a, a], color='#607285', lw=1)
ax.plot(x, y, color='#2369a3', lw=2.5)
for t in [-1.6, 1.1]:
    dt = .24
    ax.annotate('', (t+dt, np.sqrt(radius**2-(t+dt)**2)), (t, np.sqrt(radius**2-t*t)), arrowprops=dict(arrowstyle='->', color='#2369a3', lw=2))
ax.scatter([-np.pi, np.pi], [b, b], color='#b84848', s=45, zorder=4)
ax.annotate('start', (-np.pi, b), (-np.pi+.4, b-.42), color='#9a3535', ha='center', arrowprops=dict(arrowstyle='-', color='#9a3535'))
ax.annotate('same point after one turn', (np.pi, b), (np.pi-1.2, b-.42), color='#9a3535', ha='center', arrowprops=dict(arrowstyle='-', color='#9a3535'))
ax.annotate(r'$\sqrt{b^2+\pi^2}<a$', (0, radius), (0, radius+.27), ha='center')
ax.text(-np.pi-.22, (a+b)/2, 'identify', rotation=90, va='center', ha='center', color='#607285')
ax.text(np.pi+.22, (a+b)/2, 'identify', rotation=90, va='center', ha='center', color='#607285')
ax.set_xticks([-np.pi, 0, np.pi], [r'$-\pi$', '0', r'$\pi$'])
ax.set_yticks([b, a], [r'$b=\csc\beta$', r'$a=\csc\alpha$'])
ax.set_xlim(-3.75, 3.75)
ax.set_ylim(.85, 4.55)
ax.set_xlabel('unwrapped angular coordinate x')
ax.set_title('A returning geodesic in a tractoid annulus', fontsize=14, pad=15)
ax.spines[['top', 'right']].set_visible(False)
fig.tight_layout()
fig.savefig('2007-tractoid-return.png', dpi=145, facecolor='white', bbox_inches='tight')
plt.close(fig)
