"""Original binary zone-plate geometry; write the PNG to the working directory."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

h, c, electron_charge = 6.62607015e-34, 299792458., 1.602176634e-19
wavelength = h*c/(35000*electron_charge)
focal_length = .01
n = np.arange(13)
radii = np.sqrt(n*focal_length*wavelength+n*n*wavelength**2/4)*1e6
fig, ax = plt.subplots(figsize=(6, 6), facecolor='white', layout='constrained')
for k in range(12, 0, -1):
    ax.add_patch(Circle((0, 0), radii[k], facecolor='#263b53' if k % 2 == 0 else 'white', edgecolor='#263b53', linewidth=.5))
ax.plot([0, radii[-1]], [0, 0], color='#d0771d', lw=1.2)
ax.annotate(r'$r_{12}$', (.67*radii[-1], .10), color='#9a4f0c', fontsize=13)
ax.set(xlim=(-2.35, 2.35), ylim=(-2.35, 2.35), xlabel=r'$x$ ($\mu$m)', ylabel=r'$y$ ($\mu$m)', title='Alternating transmitting and opaque zones\n12-zone illustration; 35 keV, focal length 1 cm', aspect='equal')
fig.savefig('paper-1-gp2012-zone-plate.png', dpi=170, facecolor='white')
plt.close(fig)
