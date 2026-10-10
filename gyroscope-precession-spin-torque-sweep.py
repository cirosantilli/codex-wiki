"""Original synthetic slow-precession sweep, not measured wheel data.

Python 3.14, matplotlib 3.10.7, numpy 2.3.5. Run from _media, MPLBACKEND=Agg.
"""
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

spin = np.linspace(40., 160., 300)
I1, I3, theta = .09, .08, np.pi/3
Ls = I3 * spin
a = I1 * np.cos(theta)
fig, (ax, err) = plt.subplots(1, 2, figsize=(10, 4.5), facecolor='white')
fig.suptitle('Larger spin slows precession; larger transverse torque speeds it up', fontsize=14)
for K, color in zip((1.4715, 2.943, 4.4145), ('#1266a4', '#b72a30', '#238249')):
    disc = Ls**2 - 4*a*K
    assert np.all(disc > 0)
    exact = 2*K / (Ls + np.sqrt(disc))
    approx = K / Ls
    ax.plot(spin, exact, color=color, label=f'K = {K:.4g} N m')
    ax.plot(spin, approx, '--', color=color, alpha=.75)
    err.plot(spin, 100*(exact/approx-1), color=color)
q = 2*2.943/(8+np.sqrt(64-4*a*2.943))
ax.plot(100, q, 'ko', ms=5)
ax.annotate('worked example\n0.36864 rad/s', xy=(100, q), xytext=(112, .72),
            fontsize=10, arrowprops=dict(arrowstyle='->', color='black'))
err.plot(100, 100*(q/(2.943/8)-1), 'ko', ms=5)
err.annotate('0.208%', xy=(100, 100*(q/(2.943/8)-1)), xytext=(118, .54),
             fontsize=10, arrowprops=dict(arrowstyle='->', color='black'))
for panel in (ax, err):
    panel.set_xlabel('Axial spin ω₃ (rad/s)', fontsize=11)
    panel.set_xlim(40, 160)
    panel.grid(alpha=.2)
    panel.spines[['top', 'right']].set_visible(False)
ax.set_ylabel('Slow precession Ω (rad/s)', fontsize=11)
ax.set_ylim(0, 1.6)
ax.legend(frameon=False, fontsize=10, loc='upper right')
ax.text(.02, .98, 'solid: slow quadratic root\ndashed: K / (I₃ ω₃)', va='top',
        transform=ax.transAxes, fontsize=10)
err.set_ylabel('100 × (Ωslow / Ωapprox − 1) (%)', fontsize=11)
err.set_ylim(0, 2.2)
fig.text(.5, .045, 'Synthetic calculations, not measurements • θ = 60° • I₁ = 0.090, I₃ = 0.080 kg m²\n'
         'τ = K sin θ; torque coefficient K varies independently at fixed inertia',
         ha='center', fontsize=10)
fig.subplots_adjust(left=.08, right=.97, bottom=.24, top=.86, wspace=.35)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=130, facecolor='white')
plt.close(fig)
