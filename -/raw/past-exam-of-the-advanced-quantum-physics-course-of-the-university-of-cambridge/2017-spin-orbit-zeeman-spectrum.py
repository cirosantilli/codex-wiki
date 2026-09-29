"""Original exact l=1, s=1/2 Zeeman spectrum, K>0.

Python 3.14; matplotlib 3.10.7; numpy 2.3.5. PNG is written to cwd.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5.2, 800)
rp = np.sqrt((x + 1)**2 + 8)
rm = np.sqrt((x - 1)**2 + 8)
curves = [
    (1 + 2*x, r'$(3/2,3/2)$', r'$(1,1/2)$', '#0072b2', '-'),
    ((x-1+rp)/2, r'$(3/2,1/2)$', r'$(0,1/2)$', '#e69f00', '-'),
    ((x-1-rp)/2, r'$(1/2,1/2)$', r'$(1,-1/2)$', '#009e73', '--'),
    ((-x-1+rm)/2, r'$(3/2,-1/2)$', r'$(-1,1/2)$', '#cc79a7', '-'),
    ((-x-1-rm)/2, r'$(1/2,-1/2)$', r'$(0,-1/2)$', '#d55e00', '--'),
    (1-2*x, r'$(3/2,-3/2)$', r'$(-1,-1/2)$', '#333333', '-'),
]
fig, ax = plt.subplots(figsize=(8, 5.4), layout='constrained', facecolor='white')
for y, low_label, high_label, color, style in curves:
    ax.plot(x, y, color=color, ls=style, lw=2, label=low_label)
    ax.text(5.3, y[-1], high_label, color=color, va='center', fontsize=10)
ax.text(5.3, 9.3, r'$(m_\ell,m_s)$', fontsize=11)
ax.axvline(1, color='#999999', lw=1, ls=':')
ax.text(1.07, 10.4, r'$\mu_BB=K$', fontsize=10, color='#555555')
ax.set(xlim=(-0.08, 6.8), ylim=(-10.4, 12), xlabel=r'$\mu_BB/K$',
       ylabel=r'$E/K$', title=r'Spin–orbit to Paschen–Back crossover ($K>0$)')
ax.legend(title=r'Zero-field labels $(j,m_j)$', loc='lower left', ncols=2,
          fontsize=9, title_fontsize=10, framealpha=0.95)
ax.grid(alpha=0.15)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
