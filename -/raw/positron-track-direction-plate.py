"""Generate an ideal track-direction diagram, not a historical photograph.

Tested with Python 3.14, NumPy 2.3.5, Matplotlib 3.10.7.
Run from _media; output is written to the current directory.
"""
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

plt.rcParams.update({'font.size': 11, 'figure.facecolor': 'white', 'axes.facecolor': 'white'})
fig, (ax, signs) = plt.subplots(1, 2, figsize=(9.6, 5.8), gridspec_kw={'width_ratios': [1.25, 1]})
fig.suptitle('A passive plate supplies the missing direction of travel', fontsize=15, y=.97)
blue, orange = '#1768ac', '#bd4b00'
# Upward motion, B out of page, positive charge: clockwise bending.
t0 = np.linspace(-.90, 0, 250)
t1 = np.linspace(0, 1.25, 250)
x0, y0 = 10*(1-np.cos(t0)), 10*np.sin(t0)-.18
x1, y1 = 5*(1-np.cos(t1)), 5*np.sin(t1)+.18
for x in [-2, 1, 4, 7]:
    for y in [-8, -5, -2, 2, 5]:
        ax.plot(x, y, '.', color='#c0cad0', ms=4, zorder=0)
ax.add_patch(Rectangle((-2.7, -.18), 10.5, .36, facecolor='#c7c7c7', edgecolor='#666666'))
ax.plot(x0, y0, color=blue, lw=3)
ax.plot(x1, y1, color=orange, lw=3)
ax.plot([0, 0], [-.18, .18], color='#333333', lw=2, ls=':')
for xs, ys, i, col in [(x0, y0, 145, blue), (x1, y1, 150, orange)]:
    ax.annotate('', xy=(xs[i+15],ys[i+15]), xytext=(xs[i-15],ys[i-15]), arrowprops={'arrowstyle':'-|>', 'color':col, 'lw':2.4})
ax.text(1.65, -6.9, 'Before plate\n$r=10$ cm', color=blue)
ax.text(3.9, 3.4, 'After plate\n$r=5$ cm', color=orange)
ax.annotate('lead absorber', xy=(5.5,0), xytext=(4.1,-1.8), arrowprops={'arrowstyle':'->','color':'#555555'})
ax.text(-2.4, 5.65, '$B=1$ T out of page (dots)', fontsize=10)
ax.set(xlim=(-2.7,7.8), ylim=(-8.7,6.5), xlabel='$x$ (cm)', ylabel='$y$ (cm)')
ax.set_aspect('equal')
ax.set_title('Chosen circular arcs; thinner plate is schematic', fontsize=11, pad=22)
ax.spines[['right','top']].set_visible(False)
# The identical unarrowed arc admits reversed charge and travel direction.
t = np.linspace(-.75,.75,220)
x, y = 3*(1-np.cos(t)), 3*np.sin(t)
signs.plot(x,y,color='#444444',lw=3)
signs.annotate('',xy=(-.65,.95),xytext=(-.65,-.95),arrowprops={'arrowstyle':'-|>','lw':2,'color':blue})
signs.text(-.85,1.4,'$q>0$\nupward',ha='center',color=blue)
signs.annotate('',xy=(1.55,-.95),xytext=(1.55,.95),arrowprops={'arrowstyle':'-|>','lw':2,'color':orange})
signs.text(1.75,-1.65,'$q<0$\ndownward',ha='center',color=orange)
signs.text(.4,3.0,'Same curve, two interpretations',ha='center',fontsize=12)
signs.text(.4,-3.25,'Plate selects the direction:\nsmaller radius is downstream.\nThen known field polarity fixes charge.',ha='center',va='top',linespacing=1.5)
signs.text(.4,4.0,'$+y$ up; $+x$ right; $+z$ out',ha='center')
signs.set(xlim=(-2,2.8),ylim=(-5,5))
signs.set_aspect('equal'); signs.axis('off')
fig.text(.5,.035,'Original ideal teaching model • no historical track coordinates or measured energies used',ha='center',fontsize=10)
fig.subplots_adjust(left=.08,right=.98,bottom=.14,top=.86,wspace=.27)
fig.savefig(Path.cwd() / (Path(__file__).stem+'.png'),dpi=130,facecolor='white')
plt.close(fig)
