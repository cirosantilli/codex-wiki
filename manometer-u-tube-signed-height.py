"""Draw the signed vertical head of a U-tube; Python 3.14, matplotlib 3.10.7, numpy 2.3.5."""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon

plt.rcParams.update({'font.size': 12, 'font.family': 'DejaVu Sans'})
fig, ax = plt.subplots(figsize=(9.6, 6.4), dpi=100, facecolor='white')
ax.set_facecolor('white')
blue, ink = '#2284b9', '#263b4c'
outer = np.linspace(np.pi, 2*np.pi, 101)
inner = np.linspace(0, -np.pi, 101)
leftx = np.linspace(-60, -40, 31)
rightx = np.linspace(60, 40, 31)
lefty = -30 + .03*(leftx+50)**2
righty = 30 + .03*(rightx-50)**2
points = [(-60, lefty[0]), (-60, -65)]
points += list(zip(60*np.cos(outer), -65+60*np.sin(outer)))
points += [(60, righty[0])]+list(zip(rightx, righty))+[(40, -65)]
points += list(zip(40*np.cos(inner), -65+40*np.sin(inner)))
points += [(-40, lefty[-1])]+list(zip(leftx[::-1], lefty[::-1]))
ax.add_patch(Polygon(points, closed=True, facecolor='#b9e0f1', edgecolor='none'))
for radius in [40, 60]:
 ax.plot(radius*np.cos(outer), -65+radius*np.sin(outer), color=ink, lw=2)
 for sign in [-1, 1]:
  ax.plot([sign*radius]*2, [-65, 88], color=ink, lw=2)
ax.plot(leftx, lefty, color=blue, lw=2)
ax.plot(rightx, righty, color=blue, lw=2)
# The two pressure lines terminate above the liquid, not below it.
for x in [-50, 50]:
 ax.plot([x, x], [60, 113], color=ink, lw=2)
 ax.plot([x-5, x+5], [113, 113], color=ink, lw=2)
ax.plot([-100, 100], [113, 113], color=ink, lw=2)
ax.plot([-100, 100], [140, 140], color=ink, lw=2)
ax.annotate('Flow in pipe', xy=(32, 127), xytext=(-38, 127), ha='center', va='center',
 arrowprops={'arrowstyle': '->', 'color': ink, 'lw': 2}, color=ink)
ax.text(-87, 97, r'Left port: $p_L$', ha='right', color=ink)
ax.text(87, 97, r'Right port: $p_R$', ha='left', color=ink)
ax.annotate('', xy=(-50, -15), xytext=(-50, 20), arrowprops={'arrowstyle': '->', 'lw': 2, 'color': ink})
ax.text(-82, 35, 'Higher pressure\nlower meniscus', ha='right', va='center', color=ink)
for y in [-30, 30]:
 ax.hlines(y, -73, 91, colors='#78909c', linestyles='--', lw=1)
ax.hlines(0, -72, 69, colors='#a6adb4', linestyles=':', lw=1.2)
ax.text(-83, 0, 'Equal-pressure\ndatum', ha='right', va='center', color='#5c6771')
ax.text(65, -36, r'$z_L=-30$ mm', ha='left', va='top', color=ink)
ax.text(65, 36, r'$z_R=+30$ mm', ha='left', va='bottom', color=ink)
ax.annotate('', xy=(95, 30), xytext=(95, -30), arrowprops={'arrowstyle': '<->', 'color': '#b44c28', 'lw': 2})
ax.text(103, 0, r'$\Delta h=z_R-z_L$'+'\n= 60 mm (vertical)', ha='left', va='center', color='#b44c28')
ax.hlines(-65, -59, 59, colors='#456476', linestyles=':', lw=1.5)
ax.scatter([-50, 50], [-65, -65], s=24, color=ink, zorder=4)
ax.annotate('Same-height points:\nequal liquid pressure', xy=(-50, -65), xytext=(-85, -84), ha='right', va='center', fontsize=11, color=ink, arrowprops={'arrowstyle': '->', 'color': ink, 'lw': 1})
ax.text(0, -143, r'Water model: $\rho=1000$ kg m$^{-3}$, $g=9.81$ m s$^{-2}$', ha='center', color=ink)
ax.text(0, -162, r'$p_L-p_R=\rho g\Delta h=588.6$ Pa', ha='center', color=ink, fontsize=14)
ax.set_xlim(-182, 218)
ax.set_ylim(-176, 151)
ax.set_aspect('equal')
ax.axis('off')
fig.suptitle('Pressure difference becomes a vertical height difference', y=.98, fontsize=16, color=ink)
fig.subplots_adjust(left=.02, right=.98, bottom=.03, top=.93)
fig.savefig(Path.cwd()/(Path(__file__).stem+'.png'), facecolor='white', transparent=False)
plt.close(fig)
