"""Global de Sitter conformal diagram; Python 3.14 / Matplotlib 3.10.7.

Writes paper-54-de-sitter-penrose.png to the caller's CWD.
Respects the caller's MPLCONFIGDIR; no cache configuration is changed here.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(7.4, 6.6), facecolor='white', layout='constrained')
L = np.pi
ax.fill([0, L/2, 0], [-L/2, 0, L/2], color='#e7f2f8', zorder=0)
x = np.linspace(0, L, 200)
ax.plot(x, x-L/2, '--', color='#bf7423', lw=2, label='Particle horizon: χ = T + π/2')
ax.plot(x, L/2-x, '-.', color='#5d519c', lw=2, label='Event horizon: χ = π/2 − T')
for T in [-L/2, L/2]:
    ax.plot([0, L], [T, T], color='#333333', lw=3)
ax.plot([0, 0], [-L/2, L/2], color='#2b668a', lw=3, label='Comoving observer χ = 0')
ax.plot([L, L], [-L/2, L/2], color='#333333', lw=2)
ax.text(L/2, L/2+.12, 'Future spacelike infinity  I⁺', ha='center', fontsize=12)
ax.text(L/2, -L/2-.19, 'Past spacelike infinity  I⁻', ha='center', fontsize=12)
ax.text(-.13, 0, 'North pole: regular centre', rotation=90, va='center', ha='right', fontsize=10)
ax.text(L+.12, 0, 'South pole: regular antipode', rotation=90, va='center', ha='left', fontsize=10)
ax.text(.11, .11, "Observer's\nstatic patch", fontsize=10, color='#2b668a')
# Example radial null ray: exactly 45 degrees in conformal coordinates.
ax.annotate('', (2.65, .94), (2.30, .59), arrowprops={'arrowstyle':'->', 'color':'#777777', 'lw':1.4})
ax.text(2.32, .43, 'Null rays', fontsize=10, color='#666666')
ax.set_xlim(-.31, L+.31)
ax.set_ylim(-L/2-.35, L/2+.35)
ax.set_xticks([0,L/2,L], ['0','π/2','π'])
ax.set_yticks([-L/2,0,L/2], ['−π/2','0','π/2'])
ax.set_xlabel('Radial angle χ (suppressed angular two-spheres)', fontsize=11)
ax.set_ylabel('Conformal time T', fontsize=11)
ax.set_aspect('equal')
ax.set_title('Global de Sitter spacetime', fontsize=15)
ax.legend(loc='upper center', bbox_to_anchor=(.5,-.10), fontsize=9, frameon=False)
ax.grid(alpha=.12)
fig.savefig('paper-54-de-sitter-penrose.png', dpi=140, facecolor='white', transparent=False)
plt.close(fig)
