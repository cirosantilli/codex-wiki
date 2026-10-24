"""Plot normalized physicists' Hermite functions; output PNG in the current directory.

Tested with Python 3.14, NumPy 2.3 and Matplotlib 3.10; see root pyproject.toml.
"""
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(-4.5, 4.5, 1400)
polys = [np.ones_like(x), 2*x]
for n in range(1, 3):
    polys.append(2*x*polys[-1] - 2*n*polys[-2])
fig, axes = plt.subplots(2, 2, figsize=(8, 5), sharex=True, sharey=True, facecolor='white')
colors = ['#2463a6', '#a13d49', '#31846d', '#8957a1']
for n, (ax, color) in enumerate(zip(axes.flat, colors)):
    y = np.exp(-x*x/2)*polys[n]/(np.pi**0.25*math.sqrt(2**n*math.factorial(n)))
    ax.axhline(0, color='#b8bdc4', lw=.8)
    ax.plot(x, y, color=color, lw=2)
    ax.set_title(f'n = {n}', fontsize=11)
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-.8, .9)
    ax.set_xticks([-4, -2, 0, 2, 4])
    ax.spines[['top', 'right']].set_visible(False)
    ax.grid(axis='x', color='#edf0f4', lw=.7)
for ax in axes[-1]:
    ax.set_xlabel('t')
fig.suptitle('Normalized Hermite functions', fontsize=15)
fig.text(.5, .02, r'$h_n(t)=e^{-t^2/2}H_n(t)/(\pi^{1/4}\sqrt{2^n n!})$', ha='center', fontsize=12)
fig.tight_layout(rect=[0, .07, 1, .94])
fig.savefig('2007-hermite-functions.png', dpi=145, facecolor='white', bbox_inches='tight')
plt.close(fig)
