"""Illustrate the homogeneous Darcy slab; save a PNG in the current directory.

Tested with Python 3.14.4, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media: python ../darcy-flux-and-pore-velocity.py
"""
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
import numpy as np

k, mu, rho, g = 1e-12, 1e-3, 1000.0, 9.81
length, area, phi, drop = 0.5, 0.02, 0.25, 10000.0
q = k * drop / (mu * length)
flow = area * q
v = q / phi
transit = length / v
plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
blue, orange, gray = '#166a9c', '#bb5429', '#647580'
fig = plt.figure(figsize=(9, 5.5), dpi=120)
grid = fig.add_gridspec(2, 2, height_ratios=[1.1, 1], hspace=0.6, wspace=0.36)
slab = fig.add_subplot(grid[0, :])
pressure = fig.add_subplot(grid[1, 0])
speeds = fig.add_subplot(grid[1, 1])
fig.subplots_adjust(left=0.09, right=0.96, top=0.81, bottom=0.18)
fig.suptitle('One discharge, two velocity averages', fontsize=18, y=0.97)
fig.text(0.5, 0.895, r'$k=10^{-12}\ \mathrm{m^2},\quad \mu=10^{-3}\ \mathrm{Pa\,s},\quad \phi=0.25$', ha='center', fontsize=12)
slab.set(xlim=(-0.17, 0.67), ylim=(-0.08, 0.3))
slab.axis('off')
slab.add_patch(Rectangle((0, 0), length, 0.22, fc='#edf5fa', ec=blue, lw=1.8))
for x in np.linspace(0.035, 0.465, 9):
    for y in [0.04, 0.11, 0.18]:
        slab.add_patch(Circle((x, y), 0.021, fc='#bcc6cc', ec='white', lw=0.7))
slab.annotate('', xy=(0.65, 0.11), xytext=(0.51, 0.11), arrowprops={'arrowstyle': '-|>', 'color': blue, 'lw': 2.5, 'mutation_scale': 18})
slab.text(-0.025, 0.11, 'Inlet\n10 kPa', ha='right', va='center', color=blue)
slab.text(0.59, 0.25, 'Outlet: 0 kPa', ha='center', color=blue)
slab.annotate('', xy=(0.5, -0.035), xytext=(0, -0.035), arrowprops={'arrowstyle': '<->', 'color': gray})
slab.text(0.25, -0.042, 'L = 0.50 m; bulk face area A = 0.020 m²', ha='center', va='top', fontsize=10)
slab.text(0.61, 0.018, f'Q = {flow*1e6:.2f} mL/s', ha='center', color=blue, fontsize=11)
slab.text(0.25, 0.265, 'Horizontal saturated slab (pores drawn schematically)', ha='center', fontsize=11)
x = np.linspace(0, length, 101)
pressure.plot(x, drop*(1-x/length)/1000, lw=2.5, color=blue)
pressure.set(xlim=(0, length), ylim=(0, 10.7), xlabel='Distance x (m)', ylabel='Gauge pressure (kPa)', title='Constant pressure gradient')
pressure.grid(alpha=0.2)
speeds.barh([1, 0], np.array([q, v])*1e6, color=[blue, orange], height=0.5)
speeds.set(yticks=[1, 0], yticklabels=['Darcy q', 'Pore v'], xlim=(0, 103), xlabel='Mean axial velocity (µm/s)', title='The pore mean is four times larger')
for y, value, label in [(1, q, 'Q/A = 20'), (0, v, 'q/φ = 80')]:
    speeds.text(value*1e6+2, y, label, va='center', fontsize=10)
speeds.spines[['top', 'right']].set_visible(False)
fig.text(0.5, 0.075, f'Pore volume = {phi*area*length*1000:.1f} L     |     Ideal transit time = L/v = {transit:.0f} s = {transit/3600:.2f} h', ha='center', fontsize=12)
fig.text(0.5, 0.025, 'Bulk area includes solid grains; pore velocity averages only over the fluid-filled pore volume.', ha='center', fontsize=10)
fig.savefig(Path.cwd() / (Path(__file__).stem + '.png'), facecolor='white', transparent=False)
plt.close(fig)
