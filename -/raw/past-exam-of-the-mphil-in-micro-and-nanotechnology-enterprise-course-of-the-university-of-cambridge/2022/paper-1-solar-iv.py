"""Original ideal diode calculation; Python 3.14/numpy/matplotlib.

Unit collection, ideality one, supplied photon flux/J0, explicitly assumed 298 K.
Output is a PNG basename in the current working directory.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

Q = 1.602176634e-19
KB = 1.380649e-23
T = 298.0
J0 = 3.9e-8
JPH = Q*2.88e21
VT = KB*T/Q
VOC = VT*np.log1p(JPH/J0)
v = np.linspace(-.12, .63, 1500)
dark = J0*np.expm1(v/VT)
light = dark-JPH
fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.2), layout='constrained')
fig.patch.set_facecolor('white')
ax = axes[0]
ax.plot(v, dark, color='#91709b', label='Dark')
ax.plot(v, light, color='#286a85', label='Illuminated')
ax.scatter([0, VOC], [-JPH, 0], color='#b65c38', zorder=4)
ax.annotate(r'$J_{SC}=-461.4$ A m$^{-2}$', (0, -JPH), (.08, -555),
            arrowprops={'arrowstyle': '-', 'color': '.4'}, fontsize=10)
ax.annotate(f'Open circuit: {VOC:.3f} V', (VOC, 0), (.20, 270),
            arrowprops={'arrowstyle': '->', 'color': '.4'}, fontsize=10)
ax.set(xlim=(-.12, .63), ylim=(-650, 700), xlabel='Voltage (V)',
       ylabel=r'Diode-convention current density (A m$^{-2}$)', title='Illumination shifts the curve by −Jph')
ax.legend(loc='upper left', fontsize=9)
ax = axes[1]
reverse_v = np.linspace(-.35, 0, 500)
ax.plot(reverse_v, J0*np.expm1(reverse_v/VT)/J0, color='#91709b')
ax.axhline(-1, color='.5', ls='--', lw=1, label=r'$-J_0$ saturation')
ax.set(xlabel='Voltage (V)', ylabel=r'Dark current density / $J_0$',
       title='Reverse-current detail, before breakdown', ylim=(-1.15, .1))
ax.legend(fontsize=9)
for ax in axes:
    ax.axhline(0, color='.5', lw=.7)
    ax.axvline(0, color='.5', lw=.7)
    ax.grid(alpha=.16)
fig.savefig('paper-1-solar-iv.png', dpi=150, facecolor='white')
plt.close(fig)
