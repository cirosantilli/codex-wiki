"""Original constant-efficiency model. Python 3.14, numpy 2.3.5, matplotlib 3.10.7.
Run from _media; writes the matching opaque PNG to the working directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

H = 6.62607015e-34
C = 299792458
Q = 1.602176634e-19
ETA = 0.75
LAMBDA = 650e-9
POWER = 1e-6
photon_rate = POWER * LAMBDA / (H * C)
pair_rate = ETA * photon_rate
current = Q * pair_rate
plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig = plt.figure(figsize=(10.5, 5.2), facecolor='white')
ax = fig.add_axes((.09, .19, .40, .64))
wavelength_nm = np.linspace(450, 800, 351)
responsivity = ETA * Q * wavelength_nm * 1e-9 / (H * C)
ax.plot(wavelength_nm, responsivity, color='#246d9b', lw=3)
ax.scatter([650], [current / POWER], s=55, color='#a83237', zorder=3)
ax.annotate(f'650 nm\n{current / POWER:.6f} A/W', (650, current / POWER), xytext=(490, .455), arrowprops={'arrowstyle': '->', 'color': '#666666'}, color='#a83237')
ax.set(xlabel='Wavelength (nm)', ylabel='Responsivity (A/W)', xlim=(450, 800), ylim=(.24, .52))
ax.set_xticks([450, 550, 650, 750, 800])
ax.grid(alpha=.2)
ax.set_title(r'$R=\eta q\lambda/(hc)$, with $\eta=0.75$', fontsize=14, pad=13)
flow = fig.add_axes((.55, .13, .43, .73))
flow.set(xlim=(0, 1), ylim=(0, 1))
flow.axis('off')
flow.text(.5, .97, r'650 nm, incident power $1\,\mu$W', ha='center', va='top', fontsize=14)
boxes = [(.73, f'{photon_rate / 1e12:.5f} × 10¹² photons/s', '#f9e9dc'), (.42, f'{pair_rate / 1e12:.5f} × 10¹² collected pairs/s', '#e5f0f8'), (.11, f'{current * 1e6:.6f} μA in the external circuit', '#e5f3e9')]
for y, label, color in boxes:
    flow.text(.5, y, label, ha='center', va='center', fontsize=12, bbox={'boxstyle': 'round,pad=.6', 'facecolor': color, 'edgecolor': '#777777'})
for top, bottom, label in [(.66, .49, r'collect a mean fraction $\eta=0.75$'), (.35, .18, r'multiply by $q=1.602176634\times10^{-19}$ C')]:
    flow.annotate('', (.5, bottom), (.5, top), arrowprops={'arrowstyle': '-|>', 'color': '#555555', 'lw': 1.6})
    flow.text(.5, (top+bottom)/2, label, ha='center', va='center', fontsize=10.5, bbox={'facecolor': 'white', 'edgecolor': 'none', 'pad': 2})
fig.suptitle('A conversion model: photons → collected charge → current', y=.97, fontsize=17, weight='bold')
fig.text(.5, .035, 'Constructed model only; constant efficiency on 450–800 nm is not a measured spectrum.', ha='center', fontsize=11)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), dpi=130, facecolor='white', transparent=False)
plt.close(fig)
