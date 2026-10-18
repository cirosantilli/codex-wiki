"""Original projectile geometry; Python 3.14 with repository numpy/matplotlib."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

phi, theta = np.deg2rad([20, 45])
v0 = g = 1.
tf = 2 * v0 * np.sin(theta) / (g * np.cos(phi))
t = np.linspace(0, tf, 300)
x = v0 * np.cos(theta - phi) * t
y = v0 * np.sin(theta - phi) * t - .5 * g * t**2
fig, ax = plt.subplots(figsize=(9, 5.3), facecolor='white', layout='constrained')
xx = np.linspace(-.15, 1.7, 100)
ax.fill_between(xx, -xx * np.tan(phi), -1, color='#e9e2d5')
ax.plot(xx, -xx * np.tan(phi), color='#625345', lw=2)
ax.plot(x, y, color='#176b87', lw=2.5, label='Ballistic trajectory')
ax.plot([0, .7], [0, 0], ':', color='.5')
ax.annotate('', xy=(.65 * np.cos(theta-phi), .65 * np.sin(theta-phi)), xytext=(0, 0), arrowprops={'arrowstyle':'->','lw':2,'color':'#c05229'})
ax.text(.58, .31, r'$v_0$', color='#c05229', fontsize=14)
ax.add_patch(Arc((0, 0), .65, .65, theta1=-20, theta2=25, color='#c05229', lw=1.4))
ax.text(.35, .03, r'$\theta$', fontsize=15)
ax.add_patch(Arc((0, 0), 1., 1., theta1=-20, theta2=0, color='.4', lw=1.2))
ax.text(.53, -.10, r'$\phi$', fontsize=15)
ax.annotate('Launch', xy=(0,0), xytext=(-.13,.26), fontsize=12, arrowprops={'arrowstyle':'->'})
ax.plot([x[-1]], [y[-1]], 'o', color='#176b87')
ax.annotate('Landing', xy=(x[-1],y[-1]), xytext=(1.37,-.10), fontsize=12, arrowprops={'arrowstyle':'->'})
normal = np.array([np.sin(phi), np.cos(phi)])
start = -.13 * normal
end = np.array([x[-1], y[-1]]) - .13 * normal
ax.annotate('', xy=end, xytext=start, arrowprops={'arrowstyle':'<->','color':'#176b87','lw':1.5})
mid = (start+end)/2
ax.text(mid[0], mid[1]-.03, r'$R_{\rm slope}$', ha='center', va='top', fontsize=14, color='#176b87')
ax.text(.03, .95, 'Original illustration: φ = 20°, θ = 45°\nLengths in units of v₀²/g', transform=ax.transAxes, va='top', fontsize=12)
ax.set(xlim=(-.18,1.72),ylim=(-.82,.7),aspect='equal',xlabel='Horizontal displacement',ylabel='Vertical displacement',title='Launch angle measured from the downhill slope')
ax.spines[['top','right']].set_visible(False)
fig.savefig(Path.cwd() / Path(__file__).with_suffix('.png').name, dpi=120, facecolor='white', metadata={'Software':'matplotlib'})
