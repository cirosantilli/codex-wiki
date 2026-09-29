"""Original similarity-profile sketch; Python 3.14, root NumPy/Matplotlib.
Writes a basename PNG to CWD and honors caller MPLCONFIGDIR.
"""
import numpy as np
import matplotlib.pyplot as plt
k = 12
eta = np.linspace(-1, 1, 1800)
phi = (-1)**k * np.sin(k*np.pi*eta)/(k*np.pi) - eta
velocity = (-1)**k * np.cos(k*np.pi*eta) - 1
fig, axes = plt.subplots(1, 2, figsize=(9.2, 4.0), layout='constrained')
fig.set_facecolor('white')
axes[0].plot(eta, phi, lw=2, label=r'$\phi(\eta)$')
axes[0].plot(eta, -eta, '--', color='0.5', lw=1, label=r'$-\eta$')
axes[0].set(ylabel=r'$\phi$', title='Small stream-function oscillations')
axes[0].legend(fontsize=9)
axes[1].plot(eta, velocity, color='#b45309', lw=1.6)
axes[1].set(ylabel=r'$\phi^\prime=uH^2/(Cx)$', ylim=(-2.15, .15), title='Order-one velocity oscillations')
for ax in axes:
    ax.set(xlabel=r'$\eta=y/H$', xlim=(-1, 1))
    ax.grid(alpha=.2)
    ax.axvline(-1, color='0.3', lw=2)
    ax.axvline(1, color='0.3', lw=2)
fig.suptitle(r'Expanding channel: $k=12$, $R=k^2\pi^2/4$')
fig.savefig('paper-3-expanding-channel.png', dpi=130, facecolor='white', transparent=False)
