"""Draw Minkowski's radial Penrose triangle. Python 3.14; root dependencies.

Writes paper-52-penrose.png only in the caller's working directory.
MPLCONFIGDIR is preserved; all geometry follows p=atan(t-r), q=atan(t+r).
"""
import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
fig, ax = plt.subplots(figsize=(7.5, 6.5), dpi=140, facecolor='white')
ax.set_facecolor('white')
ax.fill([0, pi, 0], [-pi, 0, pi], color='#eff6fa', zorder=0)
ax.plot([0, 0], [-pi, pi], color='#263b43', lw=2)
ax.plot([0, pi], [pi, 0], color='#a36509', lw=2.1)
ax.plot([0, pi], [-pi, 0], color='#177154', lw=2.1)
ax.scatter([0, pi, 0], [pi, 0, -pi], color='black', s=32, zorder=5)
ax.text(-.10, pi+.20, r'$i^+$: future timelike infinity', ha='left', fontsize=10)
ax.text(-.10, -pi-.34, r'$i^-$: past timelike infinity', ha='left', fontsize=10)
ax.text(pi+.12, 0, r'$i^0$', fontsize=13, va='center')
ax.text(2.45, .33, 'spacelike infinity', fontsize=9, ha='center')
ax.text(1.90, 1.53, r'$\mathcal{I}^+$: future null infinity', color='#8c5608',
        rotation=-45, ha='center', fontsize=10)
ax.text(1.88, -1.50, r'$\mathcal{I}^-$: past null infinity', color='#126546',
        rotation=45, ha='center', fontsize=10)
ax.text(-.25, 0, r'$R=0$: regular centre', rotation=90, va='center', ha='center', fontsize=10)
# One null geodesic through the centre, with incoming and outgoing radial halves.
ax.plot([pi/2, 0, pi/2], [-pi/2, 0, pi/2], '--', color='#1166ad', lw=1.6,
        label='null geodesic')
ax.annotate('', xy=(.80, .80), xytext=(.45, .45),
            arrowprops={'arrowstyle': '->', 'color': '#1166ad', 'lw': 1.5})
# A complete inertial worldline: x=0.55 t, so r=|x| in the radial quotient.
s = np.linspace(-pi/2+.001, pi/2-.001, 2201)
t = np.tan(s)
r = .55*np.abs(t)
p = np.arctan(t-r)
q = np.arctan(t+r)
T, R = p+q, q-p
ax.plot(R, T, color='#ac3740', lw=1.8, label='timelike geodesic')
ix = np.searchsorted(T, 1.8)
ax.annotate('', xy=(R[ix+15], T[ix+15]), xytext=(R[ix-15], T[ix-15]),
            arrowprops={'arrowstyle': '->', 'color': '#ac3740', 'lw': 1.5})
ax.plot([0, pi], [0, 0], ':', color='#60656a', lw=1.7, label='spacelike geodesic ($t=0$)')
ax.set_xlim(-.65, pi+.56)
ax.set_ylim(-pi-.51, pi+.52)
ax.set_aspect('equal')
ax.set_xlabel(r'$R=q-p$')
ax.set_ylabel(r'$T=q+p$')
ax.set_title('Minkowski conformal compactification', fontsize=13, pad=12)
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.legend(loc='lower right', fontsize=8.5, frameon=False, bbox_to_anchor=(1.10, .02))
fig.subplots_adjust(left=.10, right=.96, bottom=.09, top=.91)
fig.savefig('paper-52-penrose.png', facecolor='white', transparent=False)
plt.close(fig)
