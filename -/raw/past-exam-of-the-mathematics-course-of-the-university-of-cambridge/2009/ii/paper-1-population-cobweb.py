"""Generate an original dimensionless population cobweb (Python 3.14).
Outputs only paper-1-population-cobweb.png in the caller's current directory.
Uses the root NumPy/Matplotlib dependencies and caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

r = 9.0
def population_map(n):
    return r*n/(1+n)**2
upper = r/4
lower = 4*r*r/(r+4)**2
values = [1.0]
for _ in range(10):
    values.append(population_map(values[-1]))
assert np.isclose(values[1], upper) and np.isclose(values[2], lower)
assert all(lower <= value <= upper for value in values[1:])
mesh = np.unique(np.r_[np.linspace(0, 2.6, 500), 1, lower, upper])
fig, ax = plt.subplots(figsize=(6.2, 4.6), layout='constrained', facecolor='white')
ax.set_facecolor('white')
ax.axvspan(lower, upper, color='#edf3e5', label='Invariant interval for t ≥ 2')
ax.plot(mesh, population_map(mesh), color='#245b96', linewidth=2, label='F(n) = 9n / (1+n)²')
ax.plot(mesh, mesh, color='#6d6d6d', linewidth=1.2, label='Diagonal')
current = values[0]
previous_height = 0.0
for new in values[1:]:
    ax.plot([current, current, new], [previous_height, new, new], color='#c14c37', linewidth=1.3)
    previous_height = new
    current = new
for n, label, offset in [(1.0, 'n₁ = 1', (-20, 12)), (upper, 'n₂ = M', (8, 12)), (lower, 'n₃ = L', (-48, 12))]:
    ax.scatter([n], [0], color='#c14c37', s=22, zorder=5, clip_on=False)
    ax.annotate(label, (n, 0), xytext=offset, textcoords='offset points', fontsize=9)
ax.scatter([2], [2], color='#222222', s=23, zorder=5)
ax.annotate('Stable fixed point', (2, 2), xytext=(-93, 16), textcoords='offset points', fontsize=9, arrowprops={'arrowstyle': '-', 'color': '#555555'})
ax.set(xlim=(0, 2.6), ylim=(0, 2.6), xlabel='Current scaled population n = bN', ylabel='Next scaled population', title='Population cobweb and post-initial invariant bounds')
ax.legend(loc='upper left', fontsize=8, framealpha=1)
ax.grid(alpha=0.18)
fig.savefig('paper-1-population-cobweb.png', dpi=150, facecolor='white', transparent=False)
plt.close(fig)
