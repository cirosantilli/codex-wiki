"""Original drift-diffusion band calculation. Python 3.14; NumPy, Matplotlib."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

k_b, temperature, charge = 1.380649e-23, 293.15, 1.602176634e-19
viscosity, radius, field = 1e-3, 2.16e-9, 500.0
friction = 6*np.pi*viscosity*radius
diffusivity = k_b*temperature/friction
delta_velocity = charge*field/friction
run_time = .001/delta_velocity
sigma_mm = np.sqrt(2*diffusivity*run_time)*1e3
x = np.linspace(18.7, 22.3, 1501)
fig, ax = plt.subplots(figsize=(7.7, 4.6), facecolor='white')
for centre, color, label in [(20, '#2b74a8', r'$Z=20$'), (21, '#c26c30', r'$Z=21$')]:
    density = np.exp(-.5*((x-centre)/sigma_mm)**2)/(np.sqrt(2*np.pi)*sigma_mm)
    ax.plot(x, density, color=color, linewidth=2.2, label=label)
    ax.fill_between(x, 0, density, color=color, alpha=.12)
    ax.axvline(centre, ymin=0, ymax=.79, color=color, linestyle=':', linewidth=1.0)
ax.annotate('', xy=(21, 1.40), xytext=(20, 1.40), arrowprops=dict(arrowstyle='<->', color='#333333'))
ax.text(20.5, 1.45, '1.00 mm', ha='center', fontsize=11)
ax.text(.02, .87, f'$t={run_time:.0f}$ s\n'+r'$\sigma_x=0.318$ mm', transform=ax.transAxes, fontsize=11)
ax.set(xlim=(18.7, 22.3), ylim=(0, 1.60), xlabel='position from injection point (mm)',
       ylabel=r'normalized band density ($\mathrm{mm}^{-1}$)')
ax.set_title('Electrophoresis separates centres while diffusion broadens bands', fontsize=12, pad=14)
ax.legend(frameon=False, loc='upper right')
ax.spines[['top', 'right']].set_visible(False)
ax.grid(alpha=.13)
fig.subplots_adjust(left=.11, right=.98, bottom=.16, top=.86)
fig.savefig(Path.cwd()/Path(__file__).with_suffix('.png').name, dpi=150, facecolor='white')
plt.close(fig)
