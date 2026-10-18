"""Original driven/free oscillator example. Output only a PNG in CWD."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

Omega, gamma, omega, A = 2., .16, 1.9, 1.
nu = np.sqrt(Omega**2-gamma**2)
D, E = Omega**2-omega**2, 2*gamma*omega
N = D**2+E**2
x0, v0 = -A*E/N, A*D*omega/N
C = (v0+gamma*x0)/nu
tn, tp = np.linspace(-12, 0, 700), np.linspace(0, 22, 1100)
xn = A*(D*np.sin(omega*tn)-E*np.cos(omega*tn))/N
xp = np.exp(-gamma*tp)*(x0*np.cos(nu*tp)+C*np.sin(nu*tp))
fig, axes = plt.subplots(2, 1, figsize=(9, 5), sharex=True, layout='constrained', gridspec_kw={'height_ratios':[1,2]})
ax = axes[0]
ax.plot(tn, A*np.sin(omega*tn), color='#b24b24', label='drive present')
ax.plot(tp, np.zeros_like(tp), color='.4', label='drive removed')
ax.set(ylabel=r'$f(t)$', title='Illustrative parameters: '+r'$\Omega=2,\ \gamma=0.16,\ \omega=1.9,\ A=1$')
ax.legend(loc='upper right', ncols=2)
ax = axes[1]
ax.plot(tn, xn, color='#1769aa', label='bounded steady motion')
ax.plot(tp, xp, color='#168347', label='free ringdown')
env = np.hypot(x0, C)*np.exp(-gamma*tp)
ax.plot(tp, env, ':', color='.45', label=r'envelope $\propto e^{-\gamma t}$')
ax.plot(tp, -env, ':', color='.45')
ax.scatter([0], [x0], color='black', s=20, zorder=4)
ax.set(xlabel=r'$t$', ylabel=r'$x(t)$', xlim=(-12,22))
ax.legend(loc='upper right', ncols=2)
for ax in axes:
    ax.axvline(0, color='.3', lw=.8)
    ax.axhline(0, color='.7', lw=.6)
    ax.grid(alpha=.15)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white')
plt.close(fig)
