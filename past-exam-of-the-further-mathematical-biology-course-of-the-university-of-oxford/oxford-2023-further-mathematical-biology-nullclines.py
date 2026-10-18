"""Generate the nullcline figure in the working directory; Python 3.14, NumPy, Matplotlib."""
import os
os.environ.setdefault('MPLCONFIGDIR', '/tmp/oxford-2023-fmb-matplotlib')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

alpha = 0.2
v = np.linspace(-0.3, 1.15, 700)
f = lambda z: z * (alpha-z) * (z-1)
cases = [(0.4, 0.112, 'One equilibrium: k = 0.4, I = 0.112'),
         (0.2, 0.032, 'Three equilibria: k = 0.2, I = 0.032')]
fig, axes = plt.subplots(1, 2, figsize=(9.4, 3.6), layout='constrained')
for ax, (k, current, title) in zip(axes, cases):
    ax.plot(v, f(v)+current, color='#2463a4', lw=2, label=r'$\dot v=0$: $w=f(v)+I$')
    ax.plot(v, k*v, color='#cb6a23', lw=2, label=r'$\dot w=0$: $w=kv$')
    roots = np.roots([1, -1-alpha, alpha+k, -current])
    roots = np.sort(roots.real[np.abs(roots.imag)<1e-9])
    ax.scatter(roots, k*roots, s=45, color='black', zorder=4)
    ax.axhline(0, lw=0.5, color='0.7')
    ax.axvline(0, lw=0.5, color='0.7')
    ax.set(xlabel='Membrane potential v', ylabel='Recovery variable w',
           title=title, xlim=(-0.3, 1.15), ylim=(-0.16, 0.48))
    ax.legend(fontsize=8, loc='upper right')
fig.suptitle(r'FitzHugh–Nagumo nullclines ($\alpha=0.2$, $k=\beta/\gamma$)', fontsize=12)
fig.savefig('oxford-2023-further-mathematical-biology-nullclines.png', dpi=145, facecolor='white')
