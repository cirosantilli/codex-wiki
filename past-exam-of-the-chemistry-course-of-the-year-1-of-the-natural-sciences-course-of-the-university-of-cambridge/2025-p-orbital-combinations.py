"""Original signed p-orbital LCAO sections for NST IA Chemistry 2025 Q2."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

x, y = np.meshgrid(np.linspace(-5.5, 5.5, 600), np.linspace(-3.8, 3.8, 450))
a = 1.0
r_a, r_b = np.hypot(x+a, y), np.hypot(x-a, y)
pax, pbx = (x+a)*np.exp(-1.8*r_a), (x-a)*np.exp(-1.8*r_b)
pay, pby = y*np.exp(-1.8*r_a), y*np.exp(-1.8*r_b)
fields = [pax-pbx, pax+pbx, pay+pby, pay-pby]
titles = [r'$\sigma_g$: end-on, bonding', r'$\sigma_u^*$: end-on, antibonding', r'$\pi_u$: side-on, bonding', r'$\pi_g^*$: side-on, antibonding']
fig, axes = plt.subplots(2, 2, figsize=(10, 7.2), facecolor='white')
for i, (ax, field, title) in enumerate(zip(axes.flat, fields, titles)):
    f = field/np.max(np.abs(field))
    ax.contourf(x, y, f, levels=[-1.01, -.65, -.3, -.08, .08, .3, .65, 1.01], colors=['#ba652e', '#dca275', '#f2d6be', 'white', '#c6e0ed', '#7fb3ce', '#347a9f'])
    ax.contour(x, y, f, levels=[-.65, -.3, -.08, .08, .3, .65], colors='#555555', linewidths=.5)
    ax.axhline(0, color='#999999', lw=.7)
    if i in [1, 3]:ax.axvline(0, color='black', ls='--', lw=1)
    ax.scatter([-a, a], [0, 0], s=20, color='black', zorder=5)
    ax.text(-a, -.2, 'A', ha='center', fontsize=9)
    ax.text(a, -.2, 'B', ha='center', fontsize=9)
    # Labels explicitly mark the signs of visible wavefunction lobes.
    positions = [[(-2.5,0), (0,0), (2.5,0)], [(-2.5,0),(-.55,0),(.55,0),(2.5,0)], [(0,1.0),(0,-1.0)], [(-1.15,1.0),(-1.15,-1.0),(1.15,1.0),(1.15,-1.0)]][i]
    for xx, yy in positions:
        v=f[np.argmin(abs(y[:,0]-yy)), np.argmin(abs(x[0]-xx))]
        ax.text(xx, yy, '+' if v>0 else '−', ha='center', va='center', fontsize=18, weight='bold', color='black')
    ax.set_title(title, fontsize=13)
    ax.set(xlim=(-5.5,5.5), ylim=(-3.8,3.8), aspect='equal')
    ax.axis('off')
fig.text(.5, .035, 'Blue: positive amplitude. Orange: negative amplitude. Dots: nuclei.\nDashed vertical lines: additional midpoint nodes. Contours are illustrative LCAO sections.', ha='center', fontsize=10)
fig.tight_layout(rect=(0,.1,1,1), h_pad=1)
fig.savefig('2025-p-orbital-combinations.png', dpi=140, facecolor='white', bbox_inches='tight')
plt.close(fig)
