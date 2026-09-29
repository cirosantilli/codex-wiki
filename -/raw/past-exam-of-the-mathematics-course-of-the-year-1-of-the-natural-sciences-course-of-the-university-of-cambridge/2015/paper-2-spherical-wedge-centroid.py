"""Original centroid plot; Python 3.14, matplotlib 3.10.7, numpy 2.3.5.

Save the white PNG in cwd, normally the mirrored _media directory.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

b = np.linspace(.0001, 2*np.pi, 600)
f = 3*np.pi*np.sin(b/2)/(8*b)
fig, ax = plt.subplots(figsize=(6.3, 3.9), layout='constrained', facecolor='white')
ax.plot(b, f, color='#0072b2', lw=2)
ax.plot([0,2*np.pi], [3*np.pi/16,0], 'o', mfc='white', mec='#0072b2')
ax.plot(np.pi, 3/8, 'o', color='#d55e00')
ax.annotate(r'$(\pi,3/8)$', (np.pi,3/8), xytext=(3.7,.44),
            arrowprops={'arrowstyle':'-', 'color':'#777777'}, fontsize=10)
ax.set(xlim=(-.12, 2*np.pi+.12), ylim=(-.025,.65), xlabel=r'Wedge angle $\beta$',
       ylabel=r'Centroid distance $f(\beta)=\bar x/a$', title='Centroid approaches the sphere centre as the wedge opens')
ax.set_xticks([0,np.pi,2*np.pi], ['$0$',r'$\pi$',r'$2\pi$'])
ax.set_yticks([0,3/8,3*np.pi/16], ['$0$',r'$3/8$',r'$3\pi/16$'])
ax.grid(alpha=.2)
fig.savefig(Path(__file__).with_suffix('.png').name, dpi=160, facecolor='white')
