"""Calculated first-period trajectory for two equally displaced prestressed masses."""
import numpy as np
import matplotlib.pyplot as plt
s = np.linspace(0, 1, 1601)
x, y = np.cos(2*np.pi*np.sqrt(2)*s), np.cos(2*np.pi*s)
fig, ax = plt.subplots(figsize=(6.4, 6), facecolor='white', layout='constrained')
ax.plot(x, y, color='#235d87', lw=2)
for q, label, offset in [(0, 'start: 0', (-70,-25)), (.25, r'$T_y/4$', (7,12)), (.5, r'$T_y/2$', (8,12)), (.75, r'$3T_y/4$', (7,12)), (1, r'end: $T_y$', (-10,-28))]:
    point = np.array([np.cos(2*np.pi*np.sqrt(2)*q), np.cos(2*np.pi*q)])
    ax.scatter(*point, color='#c25a17' if q in (0,1) else '#235d87', marker='s' if q == 1 else 'o', s=40, zorder=4)
    ax.annotate(label, point, xytext=offset, textcoords='offset points', fontsize=11)
for q in (.13, .38, .63, .88):
    a, b = q-.012, q+.012
    ax.annotate('', (np.cos(2*np.pi*np.sqrt(2)*b),np.cos(2*np.pi*b)), (np.cos(2*np.pi*np.sqrt(2)*a),np.cos(2*np.pi*a)), arrowprops=dict(arrowstyle='->',color='#235d87',lw=1.8))
ax.axhline(0, color='.8', lw=.8); ax.axvline(0, color='.8', lw=.8)
ax.set(xlim=(-1.18,1.18), ylim=(-1.18,1.18), xlabel=r'$(x_1-2l)/\epsilon$', ylabel=r'$y_1/\epsilon$', title='One transverse period; frequency ratio '+r'$\sqrt{2}$', aspect='equal')
fig.savefig('paper-1-gp2012-spring-trajectory.png', dpi=170, facecolor='white')
plt.close(fig)
