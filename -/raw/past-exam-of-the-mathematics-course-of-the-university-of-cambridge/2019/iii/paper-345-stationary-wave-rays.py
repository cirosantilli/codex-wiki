"""Plot stationary internal-wave phase contours and laboratory rays.

Run from the output directory. Tested with Python 3.14, NumPy 2.3.5,
Matplotlib 3.10.7. The figure shows original model calculations.
"""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

K = 6.0
S = 12.0
fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.8), dpi=100, layout='constrained')
fig.set_facecolor('white')
for ax, gamma, title in zip(axes, (-0.4, 0.4),
                           ('Decreasing U/N: critical level', 'Increasing U/N: turning level')):
    end = 2.46 if gamma < 0 else 2.499
    z = np.linspace(0, end, 2400)
    delta = 1 + gamma*z
    m = np.sqrt(S*S/delta**2 - K*K)
    phase = np.zeros_like(z)
    phase[1:] = np.cumsum((m[1:] + m[:-1]) * np.diff(z) / 2)
    x = np.linspace(0, 5.1, 700)
    ax.contour(x, z, K*x[None, :] + phase[:, None],
               levels=np.arange(0, 125, 2*np.pi), colors='#657b91', linewidths=0.8)
    ray = (np.sqrt(S*S-K*K) - np.sqrt(S*S-K*K*delta**2))/(K*gamma)
    for offset in (0.2, 1.2):
        ax.plot(offset+ray, z, color='#b83232', lw=1.8)
        for zh in (0.55, 1.65):
            index = np.searchsorted(z, zh)
            # Laboratory group velocity is parallel to the local wavevector.
            direction = np.array((K, m[index]))
            direction /= np.linalg.norm(direction)
            px = offset+ray[index]
            if px < 4.85:
                ax.annotate('', xy=(px+.23*direction[0], zh+.23*direction[1]),
                            xytext=(px, zh), arrowprops=dict(arrowstyle='->', color='#b83232', lw=1.7))
    for px, zh in ((3.8, .65), (3.8, 1.9)):
        mh = np.sqrt(S*S/(1+gamma*zh)**2-K*K)
        direction = np.array((K, mh))/np.hypot(K, mh)
        ax.annotate('', xy=(px+.42*direction[0], zh+.42*direction[1]),
                    xytext=(px, zh), arrowprops=dict(arrowstyle='->', color='#1260aa', lw=2))
        ax.text(px-.12, zh-.12, 'k', color='#1260aa', fontsize=10)
    ax.axhline(2.5, color='#222222', ls='--', lw=1.2)
    if gamma > 0:
        ax.axhspan(2.5, 2.92, color='#eeeeee')
        ax.text(2.55, 2.7, 'evanescent region', ha='center', fontsize=10)
    else:
        ax.axhspan(2.5, 2.92, color='#f4eeee')
        ax.text(2.55, 2.7, 'singular stationary limit', ha='center', fontsize=10)
    ax.set(xlim=(0, 5.1), ylim=(0, 2.92), xlabel='Horizontal distance x',
           ylabel='Height z', title=title)
    ax.text(.13, .12, 'red: lab energy ray\nblue: wavevector', fontsize=9,
            transform=ax.transAxes, bbox=dict(facecolor='white', edgecolor='none', alpha=.92))
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=100, facecolor='white', transparent=False)
plt.close(fig)
