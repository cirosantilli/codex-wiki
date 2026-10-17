"""Quartic and specified harmonic comparison potentials, in exam units."""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

alpha = np.cbrt(3.)
x = np.linspace(-1.85, 1.85, 600)
fig, ax = plt.subplots(figsize=(6.7, 4.1), layout='constrained')
ax.plot(x, x**4/2, color='#245c9f', lw=2, label='$V=x^4/2$')
ax.plot(x, alpha**2*x**2/2, color='#b45309', lw=1.9,
        label=r'$V=\alpha_*^2 x^2/2$, $\alpha_*=3^{1/3}$')
ax.plot(x, x**2/2, color='#37774b', ls='--', lw=1.7, label='$V=x^2/2$')
for a in [-alpha, alpha]:
    ax.plot(a, a**4/2, 'o', ms=4, color='#b45309')
ax.annotate(r'$|x|=\alpha_*$', (alpha, alpha**4/2), (0.25, 3.25),
            arrowprops={'arrowstyle':'->', 'color':'0.3'}, fontsize=11)
ax.set(xlabel='$x$', ylabel='potential energy', xlim=(-1.85, 1.85), ylim=(0, 5.8))
ax.set_title('The comparison depends on the harmonic frequency', fontsize=12)
ax.legend(loc='upper center', fontsize=10, frameon=False)
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path(__file__).stem+'.png', dpi=140, facecolor='white')
plt.close(fig)
