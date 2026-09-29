"""Calculated water-column scale and two independent rounding errors, using existing dependencies."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 11, 'font.family': 'DejaVu Sans'})
rho, g, q = 1000., 9.81, .001
bound = rho*g*q
u = bound/np.sqrt(6)
fig, (ax, bx) = plt.subplots(1, 2, figsize=(10, 4.8), dpi=100, facecolor='white')
for panel in (ax, bx):
 panel.set_facecolor('white')
 panel.spines[['top', 'right']].set_visible(False)
 panel.grid(alpha=.2)
h_mm = np.linspace(-80, 80, 161)
p = rho*g*h_mm/1000
ax.plot(h_mm, p, color='#2284b9', lw=2.5)
ax.axhline(0, color='#75818a', lw=.8)
ax.axvline(0, color='#75818a', lw=.8)
ax.plot([60], [588.6], 'o', color='#b44c28', ms=7)
ax.annotate('60 mm → 588.6 Pa', xy=(60, 588.6), xytext=(-62, 650),
 arrowprops={'arrowstyle': '->', 'color': '#b44c28'}, color='#b44c28')
ax.text(.04, .10, 'Slope = 9.81 Pa per mm\nSigned vertical height difference', transform=ax.transAxes)
ax.set(xlabel=r'$\Delta h=z_R-z_L$ (mm)', ylabel=r'$\Delta p=p_L-p_R$ (Pa)',
 title='Calculated height-to-pressure scale', xlim=(-83, 83), ylim=(-830, 830))
# Difference of two U(-q/2,q/2) errors: triangular density on [-q,q].
e = np.linspace(-bound, bound, 501)
density = (bound-np.abs(e))/bound**2
bx.fill_between(e, density, color='#b9e0f1')
bx.plot(e, density, color='#2284b9', lw=2.5)
for x in [-u, u]:
 bx.axvline(x, color='#b44c28', linestyle='--', lw=1.5)
bx.annotate(r'$u=4.005$ Pa', xy=(u, .05), xytext=(1.8, .083),
 color='#b44c28', arrowprops={'arrowstyle': '->', 'color': '#b44c28'})
bx.text(.05, .90, 'Two heights, each rounded to 1 mm\nIndependent uniform rounding model', transform=bx.transAxes, fontsize=10, va='top')
bx.text(.5, .08, 'Worst-case bounds: ±9.81 Pa', ha='center', transform=bx.transAxes)
bx.set(xlabel='Inferred pressure error (Pa)', ylabel=r'Probability density (Pa$^{-1}$)',
 title='Resolution model, not observed data', xlim=(-11, 11), ylim=(0, .139))
fig.suptitle(r'Water model: $\rho=1000$ kg m$^{-3}$, $g=9.81$ m s$^{-2}$', fontsize=15)
fig.tight_layout(rect=(0, 0, 1, .94), w_pad=2)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'), facecolor='white', transparent=False)
plt.close(fig)
