"""Original attractive point-well scattering curves; Python 3.14, numpy, matplotlib."""
import numpy as np
import matplotlib.pyplot as plt

g = np.linspace(0, 5, 501)
reflection = g * g / (1 + g * g)
transmission = 1 / (1 + g * g)
fig, ax = plt.subplots(figsize=(5.8, 3.6), layout='constrained')
ax.plot(g, reflection, color='#a23d25', label='Reflection R')
ax.plot(g, transmission, color='#245c94', label='Transmission T')
ax.plot([1, 1], [0, 0.5], ':', color='0.45')
ax.scatter([1], [0.5], color='0.2', s=20)
ax.set(xlabel=r'Attractive strength $g=mU/(\hbar^2k)$', ylabel='Current fraction', xlim=(0, 5), ylim=(0, 1.02), title='Fixed-energy scattering: R + T = 1')
ax.legend()
ax.grid(alpha=0.2)
fig.savefig('paper-1-delta-scattering.png', dpi=150, facecolor='white')
plt.close(fig)
