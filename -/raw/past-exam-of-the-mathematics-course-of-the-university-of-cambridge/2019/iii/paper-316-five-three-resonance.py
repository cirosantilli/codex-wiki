#!/usr/bin/env python3
"""Write a 5:3 resonant Kepler-orbit sketch in the planet's rotating frame."""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np

p, q = 3, 2
e = np.sqrt(2 * q / (5 * p - q))
a = ((p + q) / p)**(2 / 3)
phi = np.pi
varpi = phi / p
mean_anomaly = np.linspace(0, 2 * np.pi * p, 12001)
eccentric_anomaly = mean_anomaly.copy()
for _ in range(15):
    eccentric_anomaly -= (eccentric_anomaly - e * np.sin(eccentric_anomaly) - mean_anomaly) / (1 - e * np.cos(eccentric_anomaly))
x = a * (np.cos(eccentric_anomaly) - e)
y = a * np.sqrt(1 - e**2) * np.sin(eccentric_anomaly)
rotation = varpi - (p + q) / p * mean_anomaly
xr = x * np.cos(rotation) - y * np.sin(rotation)
yr = x * np.sin(rotation) + y * np.cos(rotation)
assert np.hypot(xr[-1] - xr[0], yr[-1] - yr[0]) < 1e-10

fig, ax = plt.subplots(figsize=(8.5, 6), dpi=100, facecolor='white')
ax.set_facecolor('white')
ax.plot(xr, yr, color='#24658a', lw=1.8, label='Particle trajectory')
theta = np.linspace(0, 2 * np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), ls='--', color='#aaa', lw=1, label='Planet orbital radius')
ax.scatter([0], [0], marker='*', s=170, color='#a86600', zorder=5, label='Star')
ax.scatter([1], [0], s=65, color='#ad3f32', zorder=5, label='Planet (fixed)')
peri_radius = a * (1 - e)
peri_angles = varpi + 2 * np.pi * np.arange(p) / p
ax.scatter(peri_radius * np.cos(peri_angles), peri_radius * np.sin(peri_angles),
           s=35, color='#154762', zorder=5, label='Three pericentres')
for index in [140, 1500, 4140, 5500, 8140, 9500]:
    ax.annotate('', xy=(xr[index + 70], yr[index + 70]), xytext=(xr[index], yr[index]),
                arrowprops={'arrowstyle': '->', 'color': '#154762', 'lw': 1.8})
ax.plot([0, 1.1], [0, 0], color='#555', lw=0.8)
ax.plot([0, peri_radius * np.cos(varpi)], [0, peri_radius * np.sin(varpi)], color='#555', lw=0.8)
ax.add_patch(Arc((0, 0), 0.7, 0.7, theta1=0, theta2=60, color='#8a4d24', lw=1.5))
ax.text(0.40, 0.20, r'$\phi/3$', color='#8a4d24', fontsize=12)
ax.set_aspect('equal')
ax.set_xlim(-2.4, 2.4)
ax.set_ylim(-2.4, 2.4)
ax.set_xlabel(r'$x/a_p$ in the planet frame')
ax.set_ylabel(r'$y/a_p$ in the planet frame')
ax.set_title(r'$5:3$ resonance: three particle orbits, five planet orbits')
ax.text(1.02, 0.96, r'$e=\sqrt{4/13}$' + '\n' + r'$a/a_p=(5/3)^{2/3}$' + '\n' + r'$\phi=3\theta_{\rm peri}\simeq\pi$',
        transform=ax.transAxes, va='top', fontsize=12)
ax.legend(loc='lower left', bbox_to_anchor=(1.01, 0.03), fontsize=10, frameon=False)
ax.grid(alpha=0.12)
fig.subplots_adjust(left=0.10, right=0.72, bottom=0.12, top=0.9)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=100, facecolor='white')
plt.close(fig)
