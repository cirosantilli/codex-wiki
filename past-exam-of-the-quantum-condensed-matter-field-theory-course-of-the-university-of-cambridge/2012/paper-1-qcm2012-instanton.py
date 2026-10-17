"""Original quartic well and instanton; Python 3.14, NumPy, Matplotlib.
All axes normalized by the explicitly chosen quartic model scales.
Writes the basename PNG to the current working directory.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
x = np.linspace(-1.55, 1.55, 600)
t = np.linspace(-7, 7, 800)
fig, axs = plt.subplots(1, 2, figsize=(10, 4.1), layout='constrained')
axs[0].plot(x, (x*x-1)**2, color='#326e9c')
axs[0].scatter([-1, 1], [0, 0], color='#326e9c')
axs[0].set(xlabel=r'$q/a$', ylabel=r'$V / (M\omega_0^2a^2/8)$', title='Symmetric quartic double well')
axs[1].plot(t, np.tanh(t/2), color='#a64a28')
axs[1].axhline(1, linestyle=':', color='gray')
axs[1].axhline(-1, linestyle=':', color='gray')
axs[1].set(xlabel=r'$\omega_0(s-s_0)$', ylabel=r'$q_I/a$', title='One Euclidean crossing', ylim=(-1.18, 1.18))
for ax in axs:
    ax.grid(alpha=.2)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=145, facecolor='white')
