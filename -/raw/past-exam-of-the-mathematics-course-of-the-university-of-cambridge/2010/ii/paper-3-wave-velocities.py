"""Original phase/group-velocity sketch; Python 3.14, root NumPy/Matplotlib.
Writes a basename PNG to CWD and honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(7.5, 4.2), layout='constrained')
fig.set_facecolor('white')
for j, k in enumerate([np.linspace(-4, -.22, 800), np.linspace(.22, 4, 800)]):
    ax.plot(k, -1/k**2, color='#b45309', lw=2, label=r'Phase: $c=-1/k^2$' if j==0 else None)
    ax.plot(k, 1/k**2, color='#0369a1', lw=2, label=r'Group: $c_g=1/k^2$' if j==0 else None)
ax.axhline(0, color='0.4', lw=.8)
ax.axvline(0, color='0.5', ls=':', lw=1)
ax.set(xlim=(-4, 4), ylim=(-7, 7), xlabel=r'Wavenumber $k$', ylabel='Velocity', title=r'$\omega=-\alpha/k$ with $\alpha=1$: phase left, packet right')
ax.grid(alpha=.2)
ax.legend(fontsize=9)
fig.savefig('paper-3-wave-velocities.png', dpi=130, facecolor='white', transparent=False)
