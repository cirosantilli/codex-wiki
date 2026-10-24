"""Original pressure sketch. Python 3.14; numpy 2.3.5, matplotlib 3.10.7.
Writes 2011-lubrication-pressure.png to the current working directory.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

x = np.linspace(-1, 1, 700)
p = 6*np.arctan(x)-3*np.pi/np.sqrt(2)*x/np.sqrt(1+x*x)
s = np.sqrt(np.pi**2/8-1)
px = lambda z: 6*np.arctan(z)-3*np.pi/np.sqrt(2)*z/np.sqrt(1+z*z)
fig, ax = plt.subplots(figsize=(6.4, 3.8), facecolor='white')
ax.axhline(0, color='0.55', lw=.8)
ax.axvline(0, color='0.75', lw=.7)
ax.plot(x, p, color='#2166a5', lw=2)
ax.fill_between(x, p, 0, where=p>=0, color='#dbeaf8')
ax.fill_between(x, p, 0, where=p<=0, color='#f4dcd8')
ax.scatter([-s, s], [px(-s), px(s)], color='#2166a5', zorder=5)
ax.annotate(r'$-x_*$', (-s, px(-s)), xytext=(-9, 10), textcoords='offset points')
ax.annotate(r'$x_*$', (s, px(s)), xytext=(5, -16), textcoords='offset points')
ax.set_xlim(-1, 1)
ax.set_ylim(-.26, .26)
ax.set_xlabel(r'$\widehat{x}$')
ax.set_ylabel(r'$\widehat{p}$', rotation=0, labelpad=13)
ax.set_title('Pressure in a symmetric translating lubrication gap')
ax.grid(alpha=.16)
fig.tight_layout()
fig.savefig('2011-lubrication-pressure.png', dpi=160, facecolor='white')
