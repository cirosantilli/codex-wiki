"""Plot finite-exponential Burgers states in the shock frame; PNG to cwd."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

states = np.array([-2., -.7, .5, 1.5])
origins = 4 * states
viscosity = .35
mean_outer = (states[0] + states[-1]) / 2
xi = np.linspace(-15, 13, 1800)
fig, ax = plt.subplots(figsize=(10, 4.8), dpi=100, facecolor='white')
for Z, color in zip([0, 4, 8, 14], ['#839baa', '#49949c', '#b97737', '#233f79']):
    theta = xi - mean_outer * Z
    exponent = (states[:, None] * (theta[None, :] - origins[:, None]) + states[:, None]**2 * Z / 2) / (2 * viscosity)
    exponent -= exponent.max(axis=0)
    weights = np.exp(exponent)
    q = (states[:, None] * weights).sum(axis=0) / weights.sum(axis=0)
    ax.plot(xi, q, lw=2, color=color, label=f'Z = {Z}')
for state in states:
    ax.axhline(state, color='#c3cbd1', lw=.7, zorder=0)
centre = 4 * (states[0] + states[-1])
limit = mean_outer + (states[-1] - states[0]) / 2 * np.tanh((states[-1] - states[0]) * (xi - centre) / (4 * viscosity))
ax.plot(xi, limit, '--', color='#333333', lw=1.3, label='Large-Z endpoint shock')
ax.set(xlim=(-15, 13), ylim=(-2.2, 1.7), xlabel=r'Moving coordinate $\xi=\theta+(q_1+q_N)Z/2$', ylabel='State q', title='Interior Burgers states disappear as the endpoint shock forms')
ax.set_yticks(states)
ax.legend(loc='upper left', fontsize=10)
ax.spines[['top', 'right']].set_visible(False)
ax.grid(alpha=.16)
fig.tight_layout(pad=1.4)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white', transparent=False)
plt.close(fig)
