"""Original surface-brightness calculation; Python 3.14, numpy, matplotlib.

Write the PNG basename into the current working directory, as required by Make.
"""
import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34
frequency = 6e14
area = 1.0
exposure = 100.0
central_brightness = 1.3e-19
inverse_radius = 0.05
central_photons = area * exposure * central_brightness / (h * frequency)
boundary = (1.0 - 16.0 / central_photons) / inverse_radius
r = np.linspace(0.0, 1.0 / inverse_radius, 501)
n = central_photons * (1.0 - inverse_radius * r)
fraction = 3.0 * (inverse_radius * r) ** 2 - 2.0 * (inverse_radius * r) ** 3
captured = 3.0 * (inverse_radius * boundary) ** 2 - 2.0 * (inverse_radius * boundary) ** 3

fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.5), layout='constrained')
fig.patch.set_facecolor('white')
ax = axes[0]
ax.plot(r, n, color='#245c94', linewidth=2)
ax.axhline(16.0, color='#a23d25', linestyle='--', label='Local threshold: 16 photons')
ax.axvline(boundary, color='0.4', linestyle=':')
ax.fill_between(r, 0, n, where=r <= boundary, color='#245c94', alpha=0.12)
ax.set(xlabel='Radius (arcsec)', ylabel='Expected photons per pixel', xlim=(0, 20), ylim=(0, 35), title='Ideal 100 s exposure')
ax.legend(loc='upper right', fontsize=8)
ax.text(boundary + 0.4, 3, f'{boundary:.2f} arcsec', fontsize=8, rotation=90, va='bottom')
ax = axes[1]
ax.plot(r, fraction, color='#245c94', linewidth=2)
ax.scatter([boundary], [captured], color='#a23d25', zorder=4)
ax.axvline(boundary, color='0.4', linestyle=':')
ax.hlines(captured, 0, boundary, color='#a23d25', linestyle='--')
ax.text(boundary + 0.7, captured - 0.08, f'{100 * captured:.1f}% captured', fontsize=9)
ax.set(xlabel='Aperture radius (arcsec)', ylabel='Fraction of full model flux', xlim=(0, 20), ylim=(0, 1.04), title='Cumulative annular integral')
for ax in axes:
    ax.grid(alpha=0.2)
fig.savefig('paper-1-isophotal-flux.png', dpi=150, facecolor='white')
plt.close(fig)
